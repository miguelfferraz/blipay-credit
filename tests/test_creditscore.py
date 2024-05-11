from unittest.mock import MagicMock

from src.creditscore import CreditScoreCalculator


def test_calculate_age_component():
    calculator = CreditScoreCalculator("José", 30, 1800, "Campinas")

    assert calculator._calculate_age_component() == 15.0


def test_calculate_income_component():
    calculator = CreditScoreCalculator("José", 30, 1800, "Campinas")

    assert calculator._calculate_income_component() == 36.0


def test_calculate_temperature_component():
    calculator = CreditScoreCalculator("José", 30, 1800, "Campinas")
    calculator.weather_client.get_temperature = MagicMock(return_value=30)

    assert calculator._calculate_temperature_component() == 150.0

    calculator = CreditScoreCalculator("José", 30, 1800, "Unknown City")
    calculator.weather_client.get_temperature = MagicMock(
        side_effect=Exception("Error")
    )

    try:
        calculator._calculate_temperature_component()
    except Exception as e:
        assert str(e) == "Error"


def test_calculate_score():
    calculator = CreditScoreCalculator("José", 30, 1800, "Campinas")

    calculator._calculate_age_component = MagicMock(return_value=15.0)
    calculator._calculate_income_component = MagicMock(return_value=36.0)
    calculator._calculate_temperature_component = MagicMock(return_value=150.0)

    assert calculator._calculate_score() == 201


def test_has_approved_credit():
    # Approved
    calculator = CreditScoreCalculator("José", 30, 1800, "Campinas")

    calculator._calculate_score = MagicMock(return_value=201)

    assert calculator.has_approved_credit() == (True, "Approved. Credit score of 201.")

    # Rejected
    calculator._calculate_score = MagicMock(return_value=199)

    assert calculator.has_approved_credit() == (
        False,
        "Rejected. Credit score of 199. Less than 200.",
    )

    # Rejected by age
    calculator = CreditScoreCalculator("José", 17, 1800, "Campinas")

    assert calculator.has_approved_credit() == (False, "Rejected. Age is less than 18.")
