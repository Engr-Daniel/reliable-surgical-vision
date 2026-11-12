"""Live UDP impairment relay (user-space alternative to kernel NetEm).

    sender --udp--> relay(listen_port) --[ImpairmentModel]--> receiver(target_port)

Used when the host has no ``sch_netem`` kernel module (e.g. sandboxed CI), and as a
seeded, bit-reproducible backend in its own right. Packets are forwarded at their
scheduled departure time. The realised fate of every packet is appended to
``fate_csv`` (emulator ground truth; never a feature input).

Usage:
    python -m src.network.relay --cond T3 --seed 7 --listen 5000 --target 5002 \
        --fate-csv runs/x/manifest/fate.csv --duration 60
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import heapq
import math
import os
import socket
import time

SOCK_BUF = 8 * 1024 * 1024  # keyframe bursts must not overflow the relay (pre-emulator loss)

from .impairment import ImpairmentModel
from .tiers import ALL


class Relay(asyncio.DatagramProtocol):
    def __init__(self, model: ImpairmentModel, target: tuple[str, int], fate_writer):
        self.model = model
        self.target = target
        self.fate_writer = fate_writer
        self.t0 = time.monotonic()
        self.heap: list[tuple[float, int, bytes]] = []
        self.n = 0
        self.transport = None
        self.wakeup = asyncio.Event()

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        now = time.monotonic() - self.t0
        dep, lost, qdrop = self.model.one(now, len(data))
        self.fate_writer.writerow([self.n, f"{now:.6f}", "" if math.isnan(dep) else f"{dep:.6f}",
                                   int(lost), int(qdrop), len(data)])
        if not math.isnan(dep):
            heapq.heappush(self.heap, (dep, self.n, data))
            self.wakeup.set()
        self.n += 1

    async def pump(self, out_sock):
        loop = asyncio.get_running_loop()
        while True:
            if not self.heap:
                self.wakeup.clear()
                await self.wakeup.wait()
                continue
            dep, _, data = self.heap[0]
            wait = dep - (time.monotonic() - self.t0)
            if wait > 0:
                self.wakeup.clear()
                try:
                    await asyncio.wait_for(self.wakeup.wait(), timeout=wait)
                except asyncio.TimeoutError:
                    pass
                continue
            heapq.heappop(self.heap)
            out_sock.sendto(data, self.target)
            await asyncio.sleep(0)


async def main_async(args):
    cond = ALL[args.cond]
    os.makedirs(os.path.dirname(os.path.abspath(args.fate_csv)), exist_ok=True)
    with open(args.fate_csv, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["pkt", "arrival_s", "depart_s", "lost_ge", "dropped_queue", "bytes"])
        model = ImpairmentModel(cond, args.seed)
        loop = asyncio.get_running_loop()
        relay = Relay(model, ("127.0.0.1", args.target), w)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCK_BUF)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCK_BUF)
        sock.bind(("127.0.0.1", args.listen))
        transport, _ = await loop.create_datagram_endpoint(lambda: relay, sock=sock)
        task = asyncio.create_task(relay.pump(transport))
        try:
            await asyncio.sleep(args.duration)
        finally:
            task.cancel()
            transport.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cond", required=True, choices=sorted(ALL))
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--listen", type=int, required=True)
    ap.add_argument("--target", type=int, required=True)
    ap.add_argument("--fate-csv", required=True)
    ap.add_argument("--duration", type=float, required=True)
    asyncio.run(main_async(ap.parse_args()))


if __name__ == "__main__":
    main()
