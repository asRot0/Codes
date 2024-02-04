import numpy as np
import matplotlib.pyplot as plt

gm = np.random.geometric(0.65, 1000)

count, bins, ignored = plt.hist(gm, 40, density=True)
plt.show()