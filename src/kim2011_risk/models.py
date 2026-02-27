from __future__ import annotations

import pandas as pd
from arch import arch_model

def fit_cv(returns: pd.Series):
    """Constant volatility: modeled as mean + i.i.d. innovations (handled in notebook)."""
    # Placeholder: CV is often estimated via MLE of Normal or Student-t.
    raise NotImplementedError("CV fitting is implemented in the notebook; port here if desired.")

def fit_garch(returns: pd.Series, dist: str = "normal"):
    """Fit GARCH(1,1) with constant mean."""
    m = arch_model(returns, mean="Constant", vol="GARCH", p=1, q=1, dist=dist)
    res = m.fit(disp="off")
    return res

def fit_ar_garch(returns: pd.Series, dist: str = "normal", lags: int = 1):
    """Fit AR(lags)-GARCH(1,1). (Note: 'arch' uses AR mean; true ARMA needs extra work.)"""
    m = arch_model(returns, mean="AR", lags=lags, vol="GARCH", p=1, q=1, dist=dist)
    res = m.fit(disp="off")
    return res
