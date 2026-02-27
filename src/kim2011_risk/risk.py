from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import norm, t as student_t

def var_from_innovations(mu_t: float, sigma_t: float, alpha: float, dist: str, nu: float | None = None) -> float:
    """One-step parametric VaR for return (left tail). Returns a negative number for loss tail."""
    if dist == "normal":
        q = norm.ppf(alpha)
    elif dist in {"t", "student-t", "student_t"}:
        if nu is None:
            raise ValueError("nu is required for Student-t VaR.")
        # arch uses standardized Student-t with unit variance; adjust if needed in your notebook
        q = student_t.ppf(alpha, df=nu)
    else:
        raise ValueError(f"Unsupported dist={dist}")
    return mu_t + sigma_t * q

def avar_es_from_innovations(mu_t: float, sigma_t: float, alpha: float, dist: str, nu: float | None = None) -> float:
    """One-step AVaR/ES for return (left tail). Returns a negative number for loss tail."""
    if dist == "normal":
        q = norm.ppf(alpha)
        es = -norm.pdf(q) / alpha
        return mu_t + sigma_t * es
    elif dist in {"t", "student-t", "student_t"}:
        if nu is None:
            raise ValueError("nu is required for Student-t ES.")
        q = student_t.ppf(alpha, df=nu)
        # ES for Student-t (non-standardized). If you standardize innovations, adjust accordingly.
        pdf = student_t.pdf(q, df=nu)
        es = - (pdf * (nu + q*q) / ((nu - 1) * alpha))
        return mu_t + sigma_t * es
    else:
        raise ValueError(f"Unsupported dist={dist}")

def absolute_relative_difference(x: pd.Series, y: pd.Series) -> float:
    """Mean absolute relative difference |(x-y)/y|."""
    return float(np.mean(np.abs((x - y) / y)))
