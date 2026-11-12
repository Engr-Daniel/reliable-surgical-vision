"""Gilbert–Elliott burst-loss model.

Two-state Markov chain (Good, Bad). In the simple Gilbert form used by VISTA and by
Linux NetEm's ``gemodel`` defaults, packets are always lost in Bad (1-h = 1) and never
in Good (1-k = 0). The chain is parameterised by

    p = P(Good -> Bad),   r = P(Bad -> Good).

The pre-registration specifies tiers by (pE, mean burst length LB):

    pE = p / (p + r)          (stationary loss rate)
    LB = 1 / r                (mean number of consecutive losses)

so  r = 1 / LB  and  p = pE * r / (1 - pE).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class GEParams:
    p: float  # Good -> Bad
    r: float  # Bad -> Good
    loss_bad: float = 1.0  # 1 - h
    loss_good: float = 0.0  # 1 - k

    @classmethod
    def from_loss_and_burst(cls, p_e: float, mean_burst: float) -> "GEParams":
        if not 0.0 <= p_e < 1.0:
            raise ValueError("p_e must be in [0, 1)")
        if mean_burst < 1.0:
            raise ValueError("mean burst length must be >= 1 packet")
        if p_e == 0.0:
            return cls(p=0.0, r=1.0)
        r = 1.0 / mean_burst
        p = p_e * r / (1.0 - p_e)
        if p > 1.0:
            raise ValueError("infeasible (p_e, mean_burst): p > 1")
        return cls(p=p, r=r)

    @property
    def stationary_loss(self) -> float:
        if self.p == 0.0:
            return self.loss_good
        pi_bad = self.p / (self.p + self.r)
        return pi_bad * self.loss_bad + (1 - pi_bad) * self.loss_good

    def netem_args(self) -> str:
        """Arguments for ``tc qdisc ... netem loss gemodel`` (percentages)."""
        return (f"loss gemodel {100 * self.p:.6g}% {100 * self.r:.6g}% "
                f"{100 * self.loss_bad:.6g}% {100 * self.loss_good:.6g}%")


class GilbertElliott:
    """Seeded, stateful loss process. ``step()`` returns True if the packet is lost."""

    def __init__(self, params: GEParams, rng: np.random.Generator):
        self.params = params
        self.rng = rng
        self.bad = False

    def step(self) -> bool:
        u = self.rng.random()
        if self.bad:
            if u < self.params.r:
                self.bad = False
        else:
            if u < self.params.p:
                self.bad = True
        prob = self.params.loss_bad if self.bad else self.params.loss_good
        return bool(prob > 0.0 and self.rng.random() < prob)


def burst_lengths(lost: np.ndarray) -> np.ndarray:
    """Lengths of runs of consecutive losses in a boolean sequence."""
    lost = np.asarray(lost, dtype=bool)
    if not lost.any():
        return np.zeros(0, dtype=int)
    padded = np.concatenate([[False], lost, [False]])
    edges = np.flatnonzero(padded[1:] != padded[:-1])
    return edges[1::2] - edges[::2]
