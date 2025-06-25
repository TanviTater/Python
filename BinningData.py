from matplotlib import pyplot as plt
import numpy as np

x = np.random.randn(100)
bins = np.linspace(-5, 5, 20)
count = np.zeros_like(bins)

i = np.searchsorted(bins, x, side='right')
i = np.clip(i, 0, len(count) - 1)

np.add.at(count, i, 1)

# Use drawstyle instead of linestyle
plt.plot(bins, count, drawstyle='steps-post')
plt.title("Manual Binning Using searchsorted + add.at")
plt.show()

# Histogram using built-in method
plt.hist(x, bins, histtype='step')
plt.title("Histogram using plt.hist()")
plt.show()
