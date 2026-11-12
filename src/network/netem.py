"""Kernel NetEm backend: build (but never silently run) ``tc`` command lines.

Production backend from pipeline-spec §2. Requires a kernel with ``sch_netem`` and
``sch_tbf`` plus CAP_NET_ADMIN. The commands are returned as lists so that the run
manifest can record exactly what was applied.
"""
from __future__ import annotations

from .tiers import Condition


def tc_commands(cond: Condition, dev: str, queue_limit_ms: int = 500) -> list[list[str]]:
    if not cond.network:
        return []
    cmds = [["tc", "qdisc", "del", "dev", dev, "root"]]  # idempotent reset (may fail harmlessly)
    netem = ["netem", "limit", "10000",
             "delay", f"{cond.delay_ms:g}ms", f"{cond.jitter_ms:g}ms", "distribution", "normal"]
    netem += cond.ge.netem_args().split()
    if cond.bandwidth_mbps is None:
        cmds.append(["tc", "qdisc", "add", "dev", dev, "root", "handle", "1:"] + netem)
    else:
        # TBF (rate, tail-drop at queue_limit) as root, NetEm as child: rate first, then delay/loss
        cmds.append(["tc", "qdisc", "add", "dev", dev, "root", "handle", "1:", "tbf",
                     "rate", f"{cond.bandwidth_mbps:g}mbit", "burst", "32kbit", "latency", f"{queue_limit_ms}ms"])
        cmds.append(["tc", "qdisc", "add", "dev", dev, "parent", "1:1", "handle", "10:"] + netem)
    return cmds
