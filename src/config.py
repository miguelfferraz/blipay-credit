import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Config:
    load_dotenv()

    OPEN_WEATHER_BASE_URL: str = os.getenv("OPEN_WEATHER_BASE_URL", "")
    OPEN_WEATHER_API_KEY: str = os.getenv("OPEN_WEATHER_API_KEY", "")