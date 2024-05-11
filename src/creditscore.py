from typing import Final

from src.config import Config
from src.openweathermap import OpenWeatherMapClient


class CreditScoreCalculator:
    def __init__(
        self,
        name: str,
        age: int,
        income: int,
        city: str,
        min_age: int = 18,
        min_score: int = 200,
    ):
        self.name = name
        self.age = age
        self.income = income
        self.city = city

        self.min_age: Final = min_age
        self.min_score: Final = min_score

        self.weather_client = OpenWeatherMapClient(
            Config.OPEN_WEATHER_BASE_URL, Config.OPEN_WEATHER_API_KEY
        )

    def _calculate_age_component(self) -> float:
        """
        Calculate the age component of the score.

        Returns:
            float: Age component of the score
        """
        return self.age * 0.5

    def _calculate_income_component(self) -> float:
        """
        Calculate the income component of the score.

        Returns:
            float: Income component of the score
        """
        return (self.income / 100) * 2

    def _calculate_temperature_component(self) -> float:
        """
        Calculate the temperature component of the score.

        Returns:
            float: Temperature component of the score

        Raises:
            Exception: If the temperature can't be retrieved
        """
        try:
            temperature = self.weather_client.get_temperature(self.city)
            return temperature * 5
        except Exception as e:
            raise e

    def _calculate_score(self) -> int:
        """
        Calculate the credit score.

        Returns:
            int: The credit score
        """
        score = (
            self._calculate_age_component()
            + self._calculate_income_component()
            + self._calculate_temperature_component()
        )
        return int(round(score))

    def has_approved_credit(self) -> tuple[bool, str]:
        """
        Check if the credit is approved.

        Returns:
            tuple[bool, str]: A tuple with a boolean and a message
        """
        if self.age < self.min_age:
            return (False, f"Rejected. Age is less than {self.min_age}.")

        score = self._calculate_score()

        if score >= self.min_score:
            return (True, f"Approved. Credit score of {score}.")

        return (
            False,
            f"Rejected. Credit score of {score}. Less than {self.min_score}.",
        )
