import pandas as pd
import pytest

from portfolio import analyse_portfolio


def test_constant_prices_have_zero_return_and_risk():
    prices = pd.DataFrame({"A": [100, 100, 100, 100], "B": [50, 50, 50, 50]})
    results = analyse_portfolio(prices, [0.5, 0.5])
    assert results["total_return"] == pytest.approx(0)
    assert results["annual_volatility"] == pytest.approx(0)
    assert results["max_drawdown"] == pytest.approx(0)


def test_growth_and_drawdown():
    prices = pd.DataFrame({"A": [100, 110, 99, 108.9]})
    results = analyse_portfolio(prices, [1.0])
    assert results["total_return"] == pytest.approx(0.089)
    assert results["max_drawdown"] == pytest.approx(-0.1)


def test_invalid_weights():
    prices = pd.DataFrame({"A": [100, 101, 102], "B": [50, 51, 52]})
    with pytest.raises(ValueError):
        analyse_portfolio(prices, [0.8, 0.8])
    with pytest.raises(ValueError):
        analyse_portfolio(prices, [1.0])
