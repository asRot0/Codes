import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(12).reshape((4, 3))
perm = np.random.permutation(arr)

count, bins, ignored = plt.hist(perm, 14, density=True)
plt.show()