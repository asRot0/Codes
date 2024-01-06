import numpy as np

arr = np.zeros((1, 2, 3, 4))
print(arr)

arr2 = np.moveaxis(arr, 0, -1)
print(arr2)
print(arr2.shape)

arr = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
print(arr)
print(np.swapaxes(arr, 0, 2))
