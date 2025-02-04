import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def check_residuals(residuals):
    p_value = stats.shapiro(residuals)[1]
    if p_value < 0.05:
        print("Residuals are not normally distributed")
    else:
        print("Residuals are normally distributed")

def qqplot(data):
    fig, ax = plt.subplots(figsize=(7, 5))
    stats.probplot(data, dist="norm", plot=ax)
    ax.set_title("Q-Q Plot of Residuals", pad=10)
    plt.xlabel("Theoretical Quantiles")
    plt.ylabel("Sample Quantiles")
    plt.tight_layout()
    plt.show()