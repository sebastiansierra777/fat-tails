# %%--------------------------------------------------------------------
# TESLA HISTOGRAM + NORMAL PDF OVERLAY
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from pathlib import Path

# Establish Excel Path
ROOT = Path(__file__).resolve().parent.parent
excel_path = ROOT / "data" / "processed" / "fat_tails.xlsx"

# Load the data
df = pd.read_excel(excel_path, sheet_name="tesla_log")

# Extract the log-return series into a Numpy array
returns = df['log_return'].dropna().values

# Compute mean and std dev from Data to derive the Fitted Normal PDF
mu = returns.mean()
sigma = returns.std(ddof=1)

# Create range for plotting the normal PDF
x = np.linspace(returns.min(), returns.max(), 500)
normal_pdf = stats.norm.pdf(x, mu, sigma)

# Plot histogram of empirical returns
fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(
    returns,
    bins=30,
    density=True,
    alpha=0.7,
    label="Empirical Distribution (Histogram of Returns)"
)

# Fitted Normal Density
ax.plot(x,
        normal_pdf,
        linewidth=3,
        label=fr"Fitted Normal Density ($\mu={mu:.4f}$, $\sigma={sigma:.4f}$)"
)

ax.set_xlabel("Tesla Daily Log Returns", fontsize=12)
ax.set_ylabel("Probability Density", fontsize=12)
ax.set_title("TSLA: Empirical Distribution vs Fitted Normal Density", fontsize=14)

# Legend
ax.legend(frameon=False, loc="best")

# Grid
ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)


# Ticks
ax.tick_params(axis="both", which="both", direction="out", length=4)


# Tight layout for better spacing
fig.tight_layout()

# Optional: save figure for reports/papers
# fig.savefig(ROOT / "figures" / "pltr_hist_fitted_normal.png", bbox_inches="tight")

plt.show()


