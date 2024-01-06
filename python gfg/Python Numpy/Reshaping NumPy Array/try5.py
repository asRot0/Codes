import numpy as np

arr = np.arange(9).reshape(3, 3)
print(arr)
print(np.vsplit(arr, 3))
print('- '*20)

arr2 = np.arange(16).reshape(4, 4)
print(arr2)
print(np.hsplit(arr2, 2))
print('- '*20)

arr3 = np.arange(27).reshape(3, 3, 3)
print(arr3)
print(np.hsplit(arr3, 3))
