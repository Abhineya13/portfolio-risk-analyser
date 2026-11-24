# Portfolio Risk Analyser

A small Python project that calculates basic portfolio performance and risk statistics using sample daily prices. Built to practise financial data analysis with pandas, NumPy and Matplotlib.

## Features

- Daily percentage returns and an **equal-weighted, daily-rebalanced** portfolio
- Total return and annualised volatility (252 trading days)
- Sharpe ratio based on geometric annualised return, assuming a **0% risk-free rate**
- Maximum drawdown (largest decline from a previous peak)
- Portfolio growth chart saved as `portfolio_performance.png`
- Basic pytest tests

## Run it

```bash
pip install -r requirements.txt
python portfolio.py
```

The script reads `sample_prices.csv`, prints risk metrics and saves the chart in your working directory. Run the tests with:

```bash
pytest -q
```

## Data and assumptions

The prices are **fictional examples**, not live market data or investment recommendations. All assets are equally weighted and rebalanced daily. Returns exclude transaction costs, fees, dividends and taxes. Volatility and the Sharpe ratio are simplified educational estimates. A short sample should not be used to infer real investment performance.

To experiment, replace the CSV prices or change the weights in `main()` (weights must add up to 1).
