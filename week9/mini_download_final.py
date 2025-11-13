# !/user/bin/env python3
# -*- coding: utf-8 -*-
import concurrent.futures
import pathlib
import socket
import time

URLS = [f"www.baidu.com/img/bd_logo1.png?r={i}" for i in range(100)]
SAVE_DIR = pathlib.Path("mini_final")
SAVE_DIR.mkdir(exist_ok=True)


def fetch_one(idx, host, path):
    """纯阻塞 IO，但跑在线程池里"""
    sock = socket.create_connection((host, 80), timeout=10)
    request = f"GET /{path} HTTP/1.0\r\nHost: {host}\r\n\r\n"
    sock.send(request.encode())
    data = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        data += chunk
    sock.close()
    (SAVE_DIR / f"{idx}.jpg").write_bytes(data.split(b"\r\n\r\n", 1)[1])
    return idx, len(data)


def main():
    t0 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as pool:
        futures = []
        for i, url in enumerate(URLS):
            host, path = url.split("/", 1)
            future = pool.submit(fetch_one, i, host, path)
            futures.append(future)
        for f in concurrent.futures.as_completed(futures):
            idx, size = f.result()
            print(f"\r{idx} done", end="")
    print(f"\nThreadPool+select: " f"{time.perf_counter() - t0:.2f}s")


if __name__ == "__main__":
    main()
