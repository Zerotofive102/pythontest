# -*- coding: utf-8 -*-
import pytest
import requests
from weather_cli import WeatherError, get_temp  # ① 导入 WeatherError


def test_get_temp_beijing():
    assert 0 <= get_temp("beijing") <= 50


def test_get_temp_default():
    assert 0 <= get_temp("xxx") <= 50  # 默认北京


def test_get_temp_exception(monkeypatch):
    def _mock_get(*a, **k):
        raise requests.ConnectionError("network down")

    monkeypatch.setattr("weather_cli.requests.get", _mock_get)
    with pytest.raises(WeatherError, match="获取.*失败"):
        get_temp("beijing")
