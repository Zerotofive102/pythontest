# !/user/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
import time

import requests

URLS = [f"https://www.baidu.com/img/bd_logo1.png?r={i}" for i in range(2_00)]
SAVE_DIR = pathlib.Path("sync_imgs")
SAVE_DIR.mkdir(exist_ok=True)

t0 = time.perf_counter()
for i, url in enumerate(URLS, 1):
    (SAVE_DIR / f"{i}.jpg").write_bytes(requests.get(url).content)
print(f"Sync: {time.perf_counter() - t0:.2f}s")
