#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import pathlib
import time

import aiohttp

URLS = [
    f"https://www.baidu.com/img/bd_logo1.png?r={i}"
    for i in range(200)  # 改成 200，少 1 字符
]
SAVE_DIR = pathlib.Path("imgs")
SAVE_DIR.mkdir(exist_ok=True)


async def fetch_one(sess: aiohttp.ClientSession, url: str, idx: int) -> None:
    async with sess.get(url) as resp:
        (SAVE_DIR / f"{idx}.jpg").write_bytes(await resp.read())


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, u, i) for i, u in enumerate(URLS, 1)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    t0 = time.perf_counter()
    asyncio.run(main())
    print(f"Concurrent: {time.perf_counter() - t0:.2f}s")
