"""Seeded forward-path impairment: rate limit -> delay/jitter -> Gilbert–Elliott loss.

``ImpairmentModel.schedule()`` is a pure, deterministic function of
(seed, packet arrival times, packet sizes). The live UDP relay (``relay.py``) and the
offline tests use the same code, so the realised packet fate is reproducible from the seed.

Semantics, chosen to match Linux NetEm + TBF used in sequence:
  1. Rate: packets are serialised at ``bandwidth`` (FIFO). If the queueing delay
     would exceed ``queue_limit_ms``, the packet is tail-dropped (congestion loss).
  2. Delay: ``delay + j(t)``, truncated at 0, where j(t) is a time-correlated jitter
     process: piecewise constant over ``jitter_slot_ms`` slots, AR(1) across slots with
     coefficient ``jitter_phi`` and stationary standard deviation ``jitter``. Departures
     are kept in FIFO order (no reordering; reordering is not a pre-registered factor).
     Independent per-packet jitter combined with FIFO ordering inflates delay, because
     packets queue behind the slowest earlier draw (median +105 ms at T5 in testing), so
     path delay is modelled as varying smoothly in time instead.
  3. Loss: Gilbert–Elliott, evaluated once per packet in send order.

The per-packet fate table is emulator ground truth. It is written to the run manifest
directory and must never be read by feature code (feature-spec §5, control 1).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .gilbert_elliott import GilbertElliott
from .tiers import Condition


@dataclass
class Fate:
    send_idx: np.ndarray       # packet index in send order
    depart_s: np.ndarray       # time the packet leaves the emulator (nan if dropped)
    lost_ge: np.ndarray        # dropped by the Gilbert–Elliott process
    dropped_queue: np.ndarray  # tail-dropped by the rate limiter

    @property
    def delivered(self) -> np.ndarray:
        return ~(self.lost_ge | self.dropped_queue)


class ImpairmentModel:
    def __init__(self, cond: Condition, seed: int, queue_limit_ms: float = 500.0,
                 jitter_slot_ms: float = 20.0, jitter_phi: float = 0.8):
        self.cond = cond
        self.jitter_slot_ms = jitter_slot_ms
        self.jitter_phi = jitter_phi
        self._slot = None
        self._j = 0.0
        self.seed = seed
        self.queue_limit_ms = queue_limit_ms
        self.rng = np.random.default_rng(seed)
        self.ge = GilbertElliott(cond.ge, self.rng)
        self._link_free_at = 0.0
        self._last_depart = 0.0

    def one(self, arrival_s: float, size_bytes: int) -> tuple[float, bool, bool]:
        """Process one packet. Returns (depart_s or nan, lost_ge, dropped_queue)."""
        c = self.cond
        if not c.network:
            return arrival_s, False, False
        # 1. rate limiting
        start = max(arrival_s, self._link_free_at)
        if c.bandwidth_mbps is not None:
            if (start - arrival_s) * 1000.0 > self.queue_limit_ms:
                # draw GE anyway so the loss process does not depend on congestion
                self.ge.step()
                return float("nan"), False, True
            tx = size_bytes * 8 / (c.bandwidth_mbps * 1e6)
            self._link_free_at = start + tx
            ready = start + tx
        else:
            ready = arrival_s
        # 2. delay + time-correlated jitter, FIFO preserved
        d = max(0.0, (c.delay_ms + self._jitter(ready)) / 1000.0)
        depart = max(ready + d, self._last_depart)
        # 3. loss
        lost = self.ge.step()
        if lost:
            return float("nan"), True, False
        self._last_depart = depart
        return depart, False, False

    def _jitter(self, t_s: float) -> float:
        """AR(1) jitter (ms), piecewise constant per slot; advances over skipped slots."""
        if self.cond.jitter_ms == 0:
            return 0.0
        slot = int(t_s * 1000.0 // self.jitter_slot_ms)
        if self._slot is None:
            self._j = self.cond.jitter_ms * self.rng.standard_normal()
        else:
            steps = min(slot - self._slot, 50)  # beyond ~50 slots the process has decorrelated
            for _ in range(max(0, steps)):
                self._j = (self.jitter_phi * self._j
                           + np.sqrt(1 - self.jitter_phi ** 2) * self.cond.jitter_ms * self.rng.standard_normal())
        self._slot = slot
        return self._j

    def schedule(self, arrival_s: np.ndarray, size_bytes: np.ndarray) -> Fate:
        n = len(arrival_s)
        dep = np.full(n, np.nan)
        lost = np.zeros(n, bool)
        qd = np.zeros(n, bool)
        for i in range(n):
            dep[i], lost[i], qd[i] = self.one(float(arrival_s[i]), int(size_bytes[i]))
        return Fate(np.arange(n), dep, lost, qd)
