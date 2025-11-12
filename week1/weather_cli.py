# -*- coding: utf-8 -*-
import requests


class WeatherError(RuntimeError):
    """天气查询相关错误基类"""


CITY_CODE = {
    "beijing": "101010100",
    "shanghai": "101020100",
    "guangzhou": "101280101",
}


def get_temp(city: str) -> float:
    """返回城市实时温度（℃）；异常时抛出 WeatherError"""
    code = CITY_CODE.get(city.lower(), "101010100")
    url = f"http://www.weather.com.cn/data/sk/{code}.html"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        resp.encoding = "utf-8"
        data = resp.json()
        return float(data["weatherinfo"]["temp"])
    except (requests.RequestException, KeyError, ValueError) as e:
        raise WeatherError(f"获取 {city} 温度失败: {e}") from e


def main() -> None:  # pragma: no cover
    city = input("请输入城市（如 beijing）：").strip() or "beijing"
    try:
        temp = get_temp(city)
        print(f"{city} 当前气温：{temp}℃")
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":  # pragma: no cover
    main()
