# !/user/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import requests


def get_weather(city: str) -> None:
    """中国天气网公开接口，免 key，http 200 稳"""
    # 城市代码字典（只列 3 个，够用即可）
    city_code = {
        "beijing": "101010100",
        "shanghai": "101020100",
        "guangzhou": "101280101",
    }
    code = city_code.get(city.lower(), "101010100")  # 默认北京
    url = f"http://www.weather.com.cn/data/sk/{code}.html"
    resp = requests.get(url, timeout=10)
    resp.encoding = "utf-8"
    data = resp.json()
    temp = data["weatherinfo"]["temp"]
    print(f"{city} 当前气温：{temp}℃")


if __name__ == "__main__":
    city = input("请输入城市（如 beijing）：").strip() or "beijing"
    get_weather(city)
