import matplotlib.pyplot as plt
import numpy as np
from variables import *
from parts import part3

x = np.linspace(mean - 4*sd, mean + 4*sd, 500)

# First distribution (the main one you're using)
y1 = stats.norm.pdf(x, loc=mean, scale=sd)

# A second distribution example (modify as needed)
# If you want only one distribution, delete this block
mean2 = mean + 0.3     # example shift
sd2 = sd * 0.9         # example change in spread
y2 = stats.norm.pdf(x, loc=mean2, scale=sd2)

# --- Plot ---
plt.figure(figsize=(10, 5))

plt.plot(x, y1, label="Distribution 1", linewidth=2)
plt.plot(x, y2, label="Distribution 2", linewidth=2)

# Optional: vertical lines at your values
plt.axvline(0, color='gray', linestyle='--', alpha=0.8)
plt.axvline(0.2, color='gray', linestyle='--', alpha=0.8)

plt.title("Overlayed Normal Distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()