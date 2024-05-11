from unittest.mock import MagicMock, patch

from src.openweathermap import OpenWeatherMapClient

BASE_URL = "http://test.com"
API_KEY = "test"


def test_get_weather_data():
    client = OpenWeatherMapClient(base_url=BASE_URL, api_key=API_KEY)

    mock_requests = MagicMock()

    with patch("src.openweathermap.requests", mock_requests):
        # Successfull response
        city = "Campinas"
        expected_weather_data = {"main": {"temp": 123.45}}

        mock_response = MagicMock()
        mock_response.json.return_value = expected_weather_data
        mock_response.status_code = 200

        mock_requests.get.return_value = mock_response

        data = client._get_weather_data(city=city)

        assert data == expected_weather_data
        mock_requests.get.assert_called_once_with(
            url="http://test.com/weather",
            params={"q": city, "appid": "test"},
            timeout=10,
        )

        # Failed response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Failed"
        mock_requests.get.return_value = mock_response

        try:
            _ = client.get_temperature(city=city)
        except Exception as e:
            assert str(e) == f"Failed to get weather data: Failed"


def test_get_temperature():
    client = OpenWeatherMapClient(base_url=BASE_URL, api_key=API_KEY)

    # Successfull response
    city = "Campinas"
    expected_temperature = 123.45

    mock_get_weather_data = MagicMock(
        return_value={"main": {"temp": expected_temperature}}
    )
    client._get_weather_data = mock_get_weather_data

    temperature = client.get_temperature(city=city)

    assert temperature == expected_temperature
    mock_get_weather_data.assert_called_once_with(city=city)

    # Failed response
    city = "Unknown"

    mock_get_weather_data = MagicMock(
        side_effect=Exception("Failed to get weather data: Failed")
    )
    client._get_weather_data = mock_get_weather_data

    try:
        _ = client.get_temperature(city=city)
    except Exception as e:
        assert str(e) == "Failed to get weather data: Failed"

    mock_get_weather_data.assert_called_once_with(city=city)
