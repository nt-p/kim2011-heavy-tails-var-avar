# Heavy‑Tailed Risk Forecasting with ARMA‑GARCH: Value‑at‑Risk and Expected Shortfall
## Replication and Empirical Validation of Kim et al. (2011)

---

# Abstract

Financial return distributions exhibit heavy tails, volatility clustering, and time‑varying variance. Classical Gaussian‑based risk models underestimate tail risk, leading to biased Value‑at‑Risk (VaR) and Expected Shortfall (ES) forecasts.

This project implements and evaluates Constant Volatility, GARCH(1,1), and ARMA(1,1)‑GARCH(1,1) models under both Gaussian and Student‑t innovations using daily S&P 500 returns. Risk forecasts are evaluated using formal statistical diagnostics including Probability Integral Transform tests, Kolmogorov‑Smirnov tests, Anderson‑Darling tests, Christoffersen coverage tests, and Berkowitz likelihood ratio tests.

Results demonstrate that heavy‑tailed models significantly improve distributional calibration and tail risk estimation.

---

# 1. Financial Motivation

Accurate tail risk estimation is fundamental to:

- Risk management
- Portfolio optimization
- Regulatory capital determination
- Stress testing
- Derivatives pricing

Financial return distributions exhibit empirical properties inconsistent with Gaussian assumptions:

$$
E[r_t^4] \gg 3\sigma^4
$$

This excess kurtosis indicates heavy tails.

Under Gaussian assumptions, extreme losses are underestimated, resulting in miscalibrated risk forecasts.

---

# 2. Data and Return Construction

Let

$$
P_t
$$

denote the asset price at time $t$.

Log returns are defined as:

$$
r_t = \ln \left( \frac{P_t}{P_{t-1}} \right)
$$

This transformation produces stationary returns suitable for volatility modelling.

---

# 3. Volatility Models

## 3.1 Constant Volatility Model

The simplest model assumes:

$$
r_t = \mu + \epsilon_t
$$

where

$$
\epsilon_t \sim D(0, \sigma^2)
$$

Variance is constant:

$$
Var(r_t) = \sigma^2
$$

This assumption is empirically invalid for financial returns.

---

## 3.2 GARCH(1,1)

The GARCH model captures volatility clustering.

Returns:

$$
r_t = \mu + \epsilon_t
$$

Innovations:

$$
\epsilon_t = \sigma_t z_t
$$

Conditional variance:

$$
\sigma_t^2 =
\omega +
\alpha \epsilon_{t-1}^2 +
\beta \sigma_{t-1}^2
$$

Stationarity condition:

$$
\alpha + \beta < 1
$$

---

## 3.3 ARMA(1,1)‑GARCH(1,1)

Mean dynamics:

$$
r_t =
\mu +
\phi r_{t-1} +
\theta \epsilon_{t-1} +
\epsilon_t
$$

Variance dynamics:

$$
\sigma_t^2 =
\omega +
\alpha \epsilon_{t-1}^2 +
\beta \sigma_{t-1}^2
$$

---

# 4. Innovation Distributions

Two innovation distributions are evaluated.

## Gaussian

$$
z_t \sim \mathcal{N}(0,1)
$$

## Student‑t

$$
z_t \sim t_\nu
$$

Student‑t distribution has heavier tails:

$$
Kurtosis = \frac{6}{\nu - 4}
$$

Heavy tails improve extreme risk modelling.

---

# 5. Risk Measures

## 5.1 Value‑at‑Risk

Value‑at‑Risk at confidence level $\alpha$ is:

$$
VaR_\alpha =
\mu_t +
\sigma_t F^{-1}(\alpha)
$$

Interpretation:

$$
P(r_t < VaR_\alpha) = \alpha
$$

---

## 5.2 Expected Shortfall

Expected Shortfall measures expected loss beyond VaR:

$$
ES_\alpha =
E[r_t | r_t < VaR_\alpha]
$$

For Gaussian:

$$
ES_\alpha =
\mu_t -
\sigma_t
\frac{\phi(\Phi^{-1}(\alpha))}{\alpha}
$$

Expected Shortfall is a coherent risk measure.

---

# 6. Statistical Validation

## 6.1 Probability Integral Transform

For correctly specified models:

$$
u_t =
F \left( \frac{\epsilon_t}{\sigma_t} \right)
$$

should follow:

$$
u_t \sim U(0,1)
$$

---

## 6.2 Kolmogorov‑Smirnov Test

Tests:

$$
H_0: F = F_{model}
$$

Rejection indicates incorrect distribution.

---

## 6.3 Anderson‑Darling Test

Sensitive to tail deviations.

Critical for financial risk modelling.

---

## 6.4 Christoffersen Coverage Test

Let violations be:

$$
I_t =
\begin{cases}
1 & r_t < VaR_t \\
0 & otherwise
\end{cases}
$$

Expected violations:

$$
E[I_t] = \alpha
$$

Likelihood ratio test evaluates coverage accuracy.

---

## 6.5 Berkowitz Test

Tests transformed residuals:

$$
z_t = \Phi^{-1}(u_t)
$$

Under correct specification:

$$
z_t \sim N(0,1)
$$

---

# 7. Empirical Results

## Distribution Fit

Gaussian innovations rejected by KS and Anderson‑Darling tests.

Student‑t innovations significantly improve distribution fit.

---

## VaR Calibration

Student‑t models produce improved coverage and independence properties.

Gaussian models underestimate extreme losses.

---

## Expected Shortfall Forecasts

![Expected Shortfall Comparison](assets/avar_comparison.png)

Student‑t models produce larger Expected Shortfall estimates during volatile periods, reflecting improved tail modelling.

---

# 8. Financial Interpretation

Heavy‑tailed models improve:

- Tail risk estimation
- Risk capital accuracy
- Extreme loss modelling

Gaussian models underestimate financial risk.

---

# 9. Implementation

Implemented using:

- Python
- numpy
- pandas
- scipy
- arch
- matplotlib
- yfinance

---

# 10. Repository Structure

```
README.md
notebooks/
report/
assets/
src/
requirements.txt
```

---

# 11. Reproducibility

Install dependencies:

```
pip install -r requirements.txt
```

Run notebook:

```
notebooks/project3_replication.ipynb
```

---

# 12. Conclusions

Heavy‑tailed models significantly improve financial risk estimation.

Distributional assumptions critically affect tail risk forecasts.

Expected Shortfall provides superior tail risk measurement.

---

# References

[Kim et al.(2011)Kim, Rachev, Bianchi, Mitov, and Fabozzi] Kim, Y. S., S. T. Rachev, M. L.
Bianchi, I. Mitov, and F. J. Fabozzi. 2011. Time series analysis for financial market
meltdowns. Journal of Banking \& Finance 35:1879–1891.

---

# Author

Neil Tamhankar

Master of Financial Mathematics

Monash University

