"""Impairment conditions, transcribed from the pre-registration (v1.1, §3 and §7.3).

Changing a value here changes the experiment: any edit must be matched by an entry
in the pre-registration amendment log.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .gilbert_elliott import GEParams


@dataclass(frozen=True)
class Condition:
    cond_id: str
    label: str
    bandwidth_mbps: float | None  # None = unconstrained
    delay_ms: float
    jitter_ms: float
    loss_pe: float
    loss_burst: float
    network: bool = True  # False = local reference (no network path)
    source: str = ""
    tags: tuple = field(default_factory=tuple)

    @property
    def ge(self) -> GEParams:
        return GEParams.from_loss_and_burst(self.loss_pe, self.loss_burst)

    @property
    def encoder_kbps(self) -> int:
        """CBR target: min(0.8 x bandwidth, 8 Mbps) (pipeline-spec §3)."""
        cap = 8000
        if self.bandwidth_mbps is None:
            return cap
        return int(min(0.8 * self.bandwidth_mbps * 1000, cap))


VISTA = "VISTA tier table (IX01, arXiv:2605.08886)"

PRIMARY = [
    Condition("T0", "Local (no network)", None, 0, 0, 0.0, 1, network=False, source="reference"),
    Condition("T1", "Hospital LAN", 100, 3, 1, 0.0001, 2, source=VISTA),
    Condition("T2", "5G Urban", 20, 35, 8, 0.005, 3, source=VISTA),
    Condition("T3", "4G Rural", 5, 150, 30, 0.02, 6, source=VISTA),
    Condition("T4", "LEO satellite", 30, 30, 10, 0.015, 5, source=VISTA),
    Condition("T5", "GEO satellite", 10, 600, 50, 0.005, 2, source=VISTA),
]

# RQ3 one-factor conditions on top of T1 (pre-registration §7.3)
_T1 = PRIMARY[1]
RQ3 = (
    [Condition(f"C-bw{b}", f"Bitrate cap {b} Mbps", b / 0.8, _T1.delay_ms, _T1.jitter_ms, _T1.loss_pe, _T1.loss_burst,
               source="prereg 7.3", tags=("compression",)) for b in (8, 4, 2, 1)]
    + [Condition(f"C-loss{str(x).replace('.', 'p')}", f"Burst loss {x}%", _T1.bandwidth_mbps, _T1.delay_ms, _T1.jitter_ms,
                 x / 100, 5, source="prereg 7.3", tags=("loss",)) for x in (0.5, 1, 2, 4)]
    + [Condition(f"C-delay{d}", f"Added delay {d} ms", _T1.bandwidth_mbps, d, 0.1 * d, _T1.loss_pe, _T1.loss_burst,
                 source="prereg 7.3", tags=("delay",)) for d in (100, 300, 600)]
)

ALL = {c.cond_id: c for c in PRIMARY + RQ3}
