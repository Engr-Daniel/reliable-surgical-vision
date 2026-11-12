"""Procedure-level cross-fitting folds (preregistration v1.1 §6)."""
from __future__ import annotations

import numpy as np

PREREG_SEED = 20261112
CHOLEC80_TRAIN = list(range(1, 33))
CHOLEC80_VAL = list(range(33, 41))
CHOLEC80_TEST = list(range(41, 81))


def procedure_folds(proc_ids, n_folds: int = 5, seed: int = PREREG_SEED) -> dict:
    """Map procedure id -> fold, via a seeded shuffle. All tiers of a procedure share a fold."""
    ids = sorted(set(proc_ids))
    rng = np.random.default_rng(seed)
    perm = rng.permutation(len(ids))
    return {ids[i]: int(k % n_folds) for k, i in enumerate(perm)}


def assert_disjoint(train_procs, test_procs):
    overlap = set(train_procs) & set(test_procs)
    if overlap:
        raise AssertionError(f"procedure leakage across folds: {sorted(overlap)}")
