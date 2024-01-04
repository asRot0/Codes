import numpy as np

arr = np.arange(12).reshape(4,3)
print(arr)

arr[:, [1,0]] = arr[:, [0,1]]

print(arr)

arr[[1,0], :] = arr[[0,1], :]

print(arr)