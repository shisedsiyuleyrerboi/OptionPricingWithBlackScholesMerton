import matplotlib.pyplot as plt
import numpy as np
from variables import *

values_p1 = [0, 0.2]

x = np.linspace(mean - 4*sd, mean + 4*sd, 500)

y = stats.norm.pdf(x, loc=mean, scale=sd)

plt.figure(figsize=(10,5))
plt.plot(x, y, label='Return Distribution', linewidth=2)

plt.axvline(values_p1[0], color='red', linestyle='--', label=f'R={values_p1[0]}')
plt.axvline(values_p1[1], color='green', linestyle='--', label=f'R={values_p1[1]}')

plt.fill_between(x, y, 0, where=(x <= values_p1[0]), color='red', alpha=0.2)
plt.fill_between(x, y, 0, where=(x >= values_p1[1]), color='green', alpha=0.2)

plt.title('Probability Distribution of Returns')
plt.xlabel('Return')
plt.ylabel('Density')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()