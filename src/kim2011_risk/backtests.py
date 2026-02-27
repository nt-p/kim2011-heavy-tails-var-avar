from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import kstest

def pit_values(residuals: np.ndarray, cdf_fn) -> np.ndarray:
    """Probability integral transform u_t = F(e_t)."""
    u = cdf_fn(residuals)
    return np.clip(u, 1e-12, 1-1e-12)

def ks_test_uniform(u: np.ndarray):
    """KS test for Uniform(0,1)."""
    return kstest(u, "uniform")

def christoffersen_lr(violations: np.ndarray, alpha: float):
    """Christoffersen LR tests: uc, ind, cc.

    violations: 0/1 array where 1 indicates loss exceeds VaR (a breach).
    """
    v = np.asarray(violations).astype(int)
    T = len(v)
    T1 = int(v.sum())
    T0 = T - T1
    # Unconditional coverage
    pi_hat = T1 / T if T > 0 else 0.0
    # Avoid log(0)
    def safe_log(x): 
        return np.log(np.clip(x, 1e-12, 1-1e-12))
    LR_uc = -2 * (T0*safe_log(1-alpha) + T1*safe_log(alpha) - (T0*safe_log(1-pi_hat) + T1*safe_log(pi_hat)))
    # Independence
    v1 = v[:-1]
    v2 = v[1:]
    T00 = int(((v1==0) & (v2==0)).sum())
    T01 = int(((v1==0) & (v2==1)).sum())
    T10 = int(((v1==1) & (v2==0)).sum())
    T11 = int(((v1==1) & (v2==1)).sum())

    pi01 = T01 / (T00+T01) if (T00+T01)>0 else 0.0
    pi11 = T11 / (T10+T11) if (T10+T11)>0 else 0.0
    pi = (T01+T11) / (T00+T01+T10+T11) if (T00+T01+T10+T11)>0 else 0.0

    LR_ind = -2 * (
        (T00+T10)*safe_log(1-pi) + (T01+T11)*safe_log(pi)
        - (T00*safe_log(1-pi01) + T01*safe_log(pi01) + T10*safe_log(1-pi11) + T11*safe_log(pi11))
    )
    LR_cc = LR_uc + LR_ind
    return {"LR_uc": float(LR_uc), "LR_ind": float(LR_ind), "LR_cc": float(LR_cc),
            "counts": {"T": T, "T1": T1, "T00": T00, "T01": T01, "T10": T10, "T11": T11}}

def berkowitz_lr(z: np.ndarray):
    """Berkowitz LR test core pieces are implemented in the notebook (AR(1) MLE).
    This placeholder exists so you can port cleanly into src/ later.
    """
    raise NotImplementedError("See notebook implementation; port here if you want a pure-python pipeline.")
