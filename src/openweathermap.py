"""Open Weather Map HTTP Client"""

from http import HTTPStatus

import requests


class OpenWeatherMapClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def _get_weather_data(self, city: str) -> dict:
        """
        Get weather data of a city

        Args:
            city (str): City name (case-insensitive)

        Returns:
            dict: Weather data

        Raises:
            Exception: If failed to get weather data
        """
        url = f"{self.base_url}/weather"
        query_params = {"q": city, "appid": self.api_key}

        res = requests.get(url=url, params=query_params, timeout=10)

        if res.status_code != HTTPStatus.OK:
            msg = f"Failed to get weather data: {res.text}"
            raise Exception(msg)

        return res.json()

    def get_temperature(self, city: str) -> float:
        """
        Get the temperature of a city

        Args:
            city (str): City name (case-insensitive)

        Returns:
            float: Temperature in Kelvin

        Raises:
            Exception: If failed to get temperature
        """
        try:
            weather_data = self._get_weather_data(city=city)

            return weather_data["main"]["temp"]
        except Exception:
            raise
