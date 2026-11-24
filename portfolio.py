"""Calculate basic portfolio performance and risk from a CSV of prices."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


DATA_FILE = Path(__file__).with_name("sample_prices.csv")


def analyse_portfolio(prices: pd.DataFrame, weights: list[float]) -> dict:
    """Return metrics for a daily-rebalanced portfolio with no transaction costs."""
    if len(weights) != prices.shape[1] or not np.isclose(sum(weights), 1.0):
        raise ValueError("Provide one weight per asset; weights must add up to 1.")
    if any(weight < 0 for weight in weights):
        raise ValueError("Weights cannot be negative in this example.")
    if len(prices) < 3 or prices.isna().any().any() or (prices <= 0).any().any():
        raise ValueError("Prices must have at least 3 rows and contain positive, non-missing values.")

    daily_returns = prices.pct_change().dropna()
    portfolio_returns = daily_returns.dot(np.asarray(weights))
    growth = (1 + portfolio_returns).cumprod()
    growth = pd.concat([pd.Series([1.0]), growth], ignore_index=True)

    total_return = growth.iloc[-1] - 1
    volatility = portfolio_returns.std(ddof=1) * np.sqrt(252)
    annual_return = growth.iloc[-1] ** (252 / len(portfolio_returns)) - 1
    sharpe = annual_return / volatility if volatility > 0 else float("nan")
    drawdown = growth / growth.cummax() - 1

    return {
        "total_return": float(total_return),
        "annual_volatility": float(volatility),
        "sharpe_ratio": float(sharpe),
        "max_drawdown": float(drawdown.min()),
        "growth": growth,
    }


def main() -> None:
    prices = pd.read_csv(DATA_FILE, index_col="Date", parse_dates=True)
    assets = list(prices.columns)
    weights = [1 / len(assets)] * len(assets)
    results = analyse_portfolio(prices, weights)

    print(f"Assets: {', '.join(assets)} (equal weights)")
    print(f"Total return: {results['total_return']:.2%}")
    print(f"Annual volatility: {results['annual_volatility']:.2%}")
    print(f"Sharpe ratio (0% risk-free rate): {results['sharpe_ratio']:.2f}")
    print(f"Maximum drawdown: {results['max_drawdown']:.2%}")

    results["growth"].plot(title="Sample Portfolio Growth", xlabel="Trading day", ylabel="Value of £1")
    plt.tight_layout()
    plt.savefig("portfolio_performance.png")
    print("Chart saved to portfolio_performance.png")


if __name__ == "__main__":
    main()
