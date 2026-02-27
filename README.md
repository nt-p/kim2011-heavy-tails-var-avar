# Heavy‑Tailed Risk Forecasting with ARMA‑GARCH: VaR and Expected Shortfall
### Replication and Extension of Kim et al. (2011)

---

# Executive Summary

This project implements and rigorously evaluates volatility‑based risk models for financial returns, focusing on the impact of distributional assumptions on tail risk estimation.

Using daily S&P 500 returns, I compare Gaussian and heavy‑tailed ARMA‑GARCH models and evaluate their ability to forecast:

- Value‑at‑Risk (VaR)
- Expected Shortfall (ES / AVaR)

using formal statistical backtests and distributional diagnostics.

The results demonstrate that Gaussian models systematically underestimate extreme risk, while heavy‑tailed models produce significantly more accurate and robust tail risk forecasts.

This finding has direct implications for:

- Risk management
- Portfolio construction
- Regulatory capital estimation
- Quantitative trading systems

---

# Financial Motivation

Financial returns are not Gaussian.

Empirical return distributions exhibit:

- Heavy tails (excess kurtosis)
- Volatility clustering
- Time‑varying variance
- Extreme events more frequent than predicted by Normal distributions

Underestimating tail risk leads to:

- Underestimated capital requirements
- Underpriced risk
- Increased exposure to catastrophic losses

This project evaluates whether heavy‑tailed volatility models improve risk estimation accuracy.

---

# Mathematical Framework

## Return Model

Returns are computed as log returns:

r_t = log(P_t / P_{t-1})

where:

- P_t = price at time t

---

## Volatility Models

### Constant Volatility Model

r_t = μ + ε_t

ε_t ~ D(0, σ²)

Assumes constant variance and independent innovations.

---

### GARCH(1,1)

Variance evolves dynamically:

σ_t² = ω + α ε_{t-1}² + β σ_{t-1}²

Captures volatility clustering.

---

### ARMA(1,1)‑GARCH(1,1)

Mean dynamics:

r_t = μ + φ r_{t-1} + θ ε_{t-1} + ε_t

Variance dynamics:

ε_t = σ_t z_t

σ_t² = ω + α ε_{t-1}² + β σ_{t-1}²

where innovations follow:

z_t ~

- Normal(0,1)
- Student‑t(ν)

---

# Risk Measures

## Value‑at‑Risk

VaR represents the α‑quantile of the return distribution.

VaR_α = μ_t + σ_t F^{-1}(α)

Interpretation:

Probability of loss exceeding VaR is α.

---

## Expected Shortfall

Expected Shortfall measures expected loss beyond VaR.

ES_α = E[r_t | r_t < VaR_α]

Advantages over VaR:

- Captures severity of losses
- Coherent risk measure
- Sensitive to tail shape

---

# Statistical Validation Framework

## Probability Integral Transform (PIT)

For correct model specification:

u_t = F(ε_t / σ_t)

should follow:

Uniform(0,1)

Deviations indicate model misspecification.

---

## Kolmogorov‑Smirnov Test

Tests:

H0: model distribution is correct

Rejecting indicates incorrect distributional assumption.

---

## Anderson‑Darling Test

More sensitive to tail behaviour than KS test.

Critical for risk modelling.

---

## Christoffersen VaR Backtests

Tests VaR calibration.

### Unconditional Coverage

Tests correct violation frequency.

Expected violations:

E[N] = αT

---

### Independence Test

Tests clustering of violations.

Violation clustering indicates poor volatility modelling.

---

### Conditional Coverage Test

Joint test combining:

- coverage accuracy
- independence

---

## Berkowitz Test

Tests full distributional calibration using transformed residuals.

Stronger than coverage tests.

---

# Empirical Results

## Distribution Fit

Gaussian innovations rejected.

Student‑t innovations provide significantly better fit.

This confirms heavy‑tailed nature of financial returns.

---

## VaR Calibration

Student‑t models show:

- Improved violation frequency
- Reduced clustering
- Better statistical calibration

Gaussian models underestimate extreme risk.

---

## Expected Shortfall Comparison

![AVaR Comparison](assets/avar_comparison.png)

Student‑t models produce:

- Larger Expected Shortfall estimates
- Greater sensitivity to volatility spikes
- More realistic tail risk forecasts

This demonstrates the critical importance of heavy‑tailed modelling.

---

# Risk Management Implications

Incorrect distribution assumptions lead to:

- Underestimated capital requirements
- Underestimated portfolio risk
- Increased exposure to extreme losses

Heavy‑tailed models improve:

- Risk estimation accuracy
- Tail risk sensitivity
- Financial robustness

---

# Technical Implementation

Implemented in Python using:

- numpy
- pandas
- scipy
- arch
- matplotlib
- yfinance

Workflow:

1. Download financial data
2. Compute returns
3. Fit volatility models
4. Forecast risk metrics
5. Perform statistical backtests
6. Compare model performance

---

# Repository Structure

.

README.md

notebooks/

report/

assets/

src/

requirements.txt

---

# Reproducibility

Install dependencies:

pip install -r requirements.txt

Run notebook:

notebooks/project3_replication.ipynb

---

# Key Conclusions

Heavy‑tailed models materially improve financial risk estimation.

Gaussian models underestimate tail risk.

Expected Shortfall provides superior risk measurement.

Distributional assumptions significantly impact financial risk forecasts.

---

# Future Extensions

Potential improvements:

- Tempered stable distributions
- Regime‑switching volatility models
- Multivariate risk modelling
- Machine learning volatility models
- Real‑time risk forecasting systems

---

# References

Kim, Y.S., Rachev, S.T., Bianchi, M.L., Mitov, I., Fabozzi, F.J.

Time series analysis for financial market meltdowns

Journal of Banking and Finance

---

# Author

Neil Tamhankar

Master of Financial Mathematics

Monash University

Quantitative Finance | Risk Modelling | Machine Learning

