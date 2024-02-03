import numpy as np
import matplotlib.pyplot as plt

num = np.random.choice(13, 5000)

count, bins, ignored = plt.hist(num, 25, density=True)
plt.show()