import numpy as np
import matplotlib.pyplot as plt

# Creating data set

# A
a = [0, 0, 1, 1, 0, 0,
     0, 1, 0, 0, 1, 0,
     1, 1, 1, 1, 1, 1,
     1, 0, 0, 0, 0, 1,
     1, 0, 0, 0, 0, 1]
# B
b = [0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 1, 0,
     0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 1, 0,
     0, 1, 1, 1, 1, 0]
# C
c = [0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 1, 1, 1, 0]

# Creating labels
y = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

for c in [a, b, c]:
    print(np.array(c).reshape(5, 6))
    plt.imshow(np.array(c).reshape(5, 6))
    plt.show()
