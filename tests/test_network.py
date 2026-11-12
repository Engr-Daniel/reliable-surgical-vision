import numpy as np
import pytest

from src.network.gilbert_elliott import GEParams, GilbertElliott, burst_lengths
from src.network.impairment import ImpairmentModel
from src.network.netem import tc_commands
from src.network.tiers import ALL, PRIMARY, RQ3


@pytest.mark.parametrize("pe,lb", [(0.0001, 2), (0.005, 3), (0.02, 6), (0.015, 5), (0.04, 5)])
def test_ge_parameterisation_roundtrip(pe, lb):
    g = GEParams.from_loss_and_burst(pe, lb)
    assert g.stationary_loss == pytest.approx(pe, rel=1e-9)
    assert 1 / g.r == pytest.approx(lb)


@pytest.mark.parametrize("pe,lb", [(0.02, 6), (0.005, 3)])
def test_ge_realised_statistics(pe, lb):
    rng = np.random.default_rng(1)
    proc = GilbertElliott(GEParams.from_loss_and_burst(pe, lb), rng)
    lost = np.array([proc.step() for _ in range(400_000)])
    assert lost.mean() == pytest.approx(pe, rel=0.15)
    assert burst_lengths(lost).mean() == pytest.approx(lb, rel=0.15)


def test_burst_lengths():
    assert burst_lengths(np.array([0, 1, 1, 0, 1, 0, 1, 1, 1], bool)).tolist() == [2, 1, 3]
    assert burst_lengths(np.zeros(5, bool)).size == 0


def test_tiers_match_preregistration():
    t = {c.cond_id: c for c in PRIMARY}
    assert [c.cond_id for c in PRIMARY] == ["T0", "T1", "T2", "T3", "T4", "T5"]
    assert (t["T3"].bandwidth_mbps, t["T3"].delay_ms, t["T3"].jitter_ms, t["T3"].loss_pe, t["T3"].loss_burst) == (5, 150, 30, 0.02, 6)
    assert (t["T5"].bandwidth_mbps, t["T5"].delay_ms) == (10, 600)
    assert t["T0"].network is False
    assert len(RQ3) == 11
    assert ALL["C-bw4"].encoder_kbps == 4000


def _cbr_stream(seconds=60, fps=25, kbps=4000, mtu=1200):
    """Synthetic packet stream: each frame split into MTU-sized packets, sent at frame time."""
    per_frame = kbps * 1000 / 8 / fps
    arr, size = [], []
    for f in range(seconds * fps):
        n = int(np.ceil(per_frame / mtu))
        for k in range(n):
            arr.append(f / fps + k * 1e-5)
            size.append(mtu)
    return np.array(arr), np.array(size)


def test_impairment_deterministic_from_seed():
    arr, size = _cbr_stream(10)
    f1 = ImpairmentModel(ALL["T3"], seed=7).schedule(arr, size)
    f2 = ImpairmentModel(ALL["T3"], seed=7).schedule(arr, size)
    f3 = ImpairmentModel(ALL["T3"], seed=8).schedule(arr, size)
    assert np.array_equal(f1.lost_ge, f2.lost_ge) and np.allclose(f1.depart_s, f2.depart_s, equal_nan=True)
    assert not np.array_equal(f1.lost_ge, f3.lost_ge)


@pytest.mark.parametrize("cid", ["T2", "T3", "T4", "T5"])
def test_impairment_realised_loss_and_delay(cid):
    c = ALL[cid]
    arr, size = _cbr_stream(120, kbps=c.encoder_kbps)
    fate = ImpairmentModel(c, seed=3).schedule(arr, size)
    # pipeline-spec §6 (b): realised loss within tolerance of configured (sampling noise at low pE)
    assert fate.lost_ge.mean() == pytest.approx(c.loss_pe, rel=0.35)
    assert not fate.dropped_queue.any(), "encoder at 0.8 x bandwidth must not congest the link"
    d = fate.depart_s - arr
    d = d[fate.delivered]
    assert np.median(d) * 1000 == pytest.approx(c.delay_ms, abs=c.jitter_ms + 5)
    # FIFO: departures of delivered packets are non-decreasing
    dep = fate.depart_s[fate.delivered]
    assert np.all(np.diff(dep) >= -1e-12)
    if c.jitter_ms > 0:
        # realised delay spread close to the configured jitter (FIFO adds little)
        assert np.std(d) * 1000 == pytest.approx(c.jitter_ms, rel=0.35)


def test_congestion_tail_drop():
    c = ALL["C-bw1"]  # 1.25 Mbit link
    arr, size = _cbr_stream(20, kbps=4000)  # deliberately oversubscribed
    fate = ImpairmentModel(c, seed=1).schedule(arr, size)
    assert fate.dropped_queue.mean() > 0.3


def test_local_reference_is_passthrough():
    arr, size = _cbr_stream(5)
    fate = ImpairmentModel(ALL["T0"], seed=1).schedule(arr, size)
    assert fate.delivered.all() and np.allclose(fate.depart_s, arr)


def test_netem_commands():
    cmds = tc_commands(ALL["T3"], "veth0")
    flat = [" ".join(c) for c in cmds]
    assert any("tbf rate 5mbit" in f for f in flat)
    assert any("delay 150ms 30ms distribution normal" in f and "loss gemodel" in f for f in flat)
    assert tc_commands(ALL["T0"], "veth0") == []
