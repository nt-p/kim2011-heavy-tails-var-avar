# Heavy-Tailed Risk Forecasting with (AR)GARCH: VaR & AVaR (Kim et al., 2011 replication)

This project replicates and extends key ideas from **Kim, Rachev, Bianchi, Mitov & Fabozzi (2011)**:
normality-based risk models systematically understate tail risk during crisis periods, and heavy-tailed
innovations improve the calibration of **Value-at-Risk (VaR)** and **Average Value-at-Risk / Expected Shortfall (AVaR/ES)**.

**What I built**
- Pulled daily S&P 500 proxy data and computed log-returns.
- Fit benchmark volatility/risk models:
  - Constant Volatility (CV)
  - GARCH(1,1) with **Normal** vs **Student-t** innovations
  - (AR)GARCH variant with an autoregressive mean component (via `arch`'s AR mean)
- Evaluated distributional adequacy and tail calibration using:
  - **Probability Integral Transform (PIT)** diagnostics
  - **Kolmogorov–Smirnov (KS)** and **Anderson–Darling (AD)** tests
  - **Christoffersen LR tests** (unconditional coverage, independence, conditional coverage)
  - **Berkowitz LR tests** (distributional calibration of PITs, tail-focused checks)
- Produced VaR/AVaR time series and divergence metrics (e.g., **Absolute Relative Difference (ARD)**).

**Key takeaway**
Heavy-tailed models (Student-t) materially improve tail risk calibration relative to Gaussian baselines,
especially at short-to-medium horizons and during stress regimes.

---

## Repository structure

```
.
├─ notebooks/
│  └─ project3_replication.ipynb
├─ report/
│  └─ Project3_Report.pdf
├─ src/
│  └─ kim2011_risk/
│     ├─ __init__.py
│     ├─ data.py
│     ├─ models.py
│     ├─ risk.py
│     ├─ backtests.py
│     └─ plots.py
├─ tests/
├─ configs/
│  └─ params.yaml
├─ requirements.txt
└─ LICENSE
```

---

## How to run (reproducible)

### 1) Create environment

```bash
python -m venv .venv
# mac/linux
source .venv/bin/activate
# windows
# .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Run the notebook

```bash
jupyter lab
# open notebooks/project3_replication.ipynb
```

---

## Results snapshot (what to highlight to recruiters)

In your GitHub README, the most recruiter-friendly story is:

1. **Problem:** Gaussian VaR fails in crises (underestimates tail loss frequency).
2. **Method:** Fit GARCH-type models with Normal vs Student-t innovations.
3. **Validation:** Use PIT + KS/AD for distribution fit; CLR/BLR for VaR calibration.
4. **Impact:** Student-t improves coverage/tail calibration; AVaR is more informative than VaR.

See `report/Project3_Report.pdf` for the full write-up and tables/figures.

---

## Limitations & next steps (planned extensions)

- Add **true ARMA(1,1)** mean (with MA term) rather than AR-only mean.
- Implement **tempered stable** innovations (CTS/MTS/RDTS) to match Kim et al. (2011) more closely.
- Use a **rolling-window** backtest (e.g., 10y rolling estimation, 1d VaR/ES forecasts).
- Compare against **EWMA** and **Filtered Historical Simulation (FHS)** baselines.
- Package the pipeline as a `python -m kim2011_risk.run` CLI script with config-driven experiments.

---

## Citation

Kim, Y. S., Rachev, S. T., Bianchi, M. L., Mitov, I., & Fabozzi, F. J. (2011).
*Time series analysis for financial market meltdowns.* Journal of Banking & Finance, 35, 1879–1891.
