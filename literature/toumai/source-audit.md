# P0.1 Source Audit

## Audit decision
P0.1 is considered **complete at the focused public-evidence reconnaissance level** after the 2026-09-25 final audit.

The completion claim means:
- the P0.1 research questions can be answered to the limit of public evidence;
- all material numeric claims in the final report are traceable;
- manufacturer and deployment claims are labelled;
- unresolved proprietary details are explicit;
- the search and screening process is reproducible.

It does **not** mean:
- every Toumai publication has been exhaustively catalogued;
- proprietary system internals are known;
- publication-level novelty has been established;
- P0.2–P0.7 can be skipped.

## Final evidence corrections relative to the earlier draft
The final audit added or corrected:
- Yang et al.: 43.4 ms delay, 4 ms jitter, 98.3 Mbps upload, 213 Mbps download, <1% packet loss.
- Zhou et al.: 216.5 Mbps down, 86.6 Mbps up, average max/min latency 129.3/20.7 ms, 0% packet loss.
- Guo FUTURE-04: 226.2 ± 4.4 ms total delay, 31.6 ± 3.8 ms network round-trip delay, <0.1% packet loss.
- Pokhrel 2026 hybrid: 12 ms median fiber latency, 46 ms median 5G latency.
- Pan 2026: primary + two carrier backups, QoS, explicit network thresholds, preoperative stress/disconnection drills, mean RTT 37.7 ± 5.6 ms, max latency 47.5 ± 5.4 ms, jitter 2.2 ± 0.5 ms, zero loss/interruptions.
- Explicit preservation of different latency definitions.
- A screening log and machine-readable network-metrics table.
- BibTeX source file.

## Confidence by domain
| Domain | P0.1 confidence | Reason |
|---|---|---|
| Core component architecture | High | Regulatory review + official product documentation |
| High-level master–slave control principle | High | Regulatory working principle |
| Local imaging feature set | High for presence | Peer-reviewed technical description |
| Haptics/4000 Hz/250 μs | Moderate–High as reported characteristics | Same paper cautions advanced-feature performance was not objectively quantified |
| Human remote-network metrics | High within each individual deployment | Multiple peer-reviewed studies |
| Universal Toumai network topology | Not supported | Deployments vary materially |
| Codec/adaptive streaming/failover thresholds | Unknown | Not publicly exposed |
| Nigerian raw network performance | Unknown | No telemetry found |
| Network→CV reliability effect | Hypothesis | Requires later empirical study |

## Gate recommendation
P0.1 can now be tagged **v0.0.1** after repository integration/review. P0.2 may begin.
