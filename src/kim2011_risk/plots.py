from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

def plot_series(df: pd.DataFrame, title: str, ylabel: str, path: str | None = None):
    ax = df.plot(figsize=(10,4))
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    if path:
        plt.savefig(path, dpi=200)
    return ax
