import matplotlib.pyplot as plt
import numpy as np

gaussian_numbers = np.random.randn(100)

plt.hist(gaussian_numbers, rwidth=1)
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()
