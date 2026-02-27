from __future__ import annotations

import pandas as pd
import numpy as np
import yfinance as yf

def load_prices(ticker: str = "^GSPC", start: str = "2000-01-01", end: str | None = None) -> pd.Series:
    """Download adjusted close prices via yfinance."""
    df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
    if df.empty:
        raise ValueError(f"No data returned for ticker={ticker}.")
    # yfinance returns a column named 'Close' when auto_adjust=True
    px = df["Close"].dropna()
    px.name = "price"
    return px

def log_returns(prices: pd.Series) -> pd.Series:
    """Compute log returns."""
    r = np.log(prices).diff().dropna()
    r.name = "log_return"
    return r
