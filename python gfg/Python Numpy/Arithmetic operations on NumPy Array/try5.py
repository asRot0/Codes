import numpy as np

arr = np.array([25, 1.33, 1, 1, 100])
print('array -- ', arr)
print('reciprocal function -- ', np.reciprocal(arr))

arr = np.array([25], dtype=int)
print('array -- ', arr)
print('reciprocal function -- ', np.reciprocal(arr))

arr = np.array([1, 2, 3])
arr1 = np.array([2, 3, 4])
print('power -- ', np.power(arr1, arr))
print('mod -- ', np.mod(arr1, arr))
print('remainder -- ', np.remainder(arr1, arr))

arr = np.arange(9).reshape(3, 3)
print('arr -- ', arr)
print('sum -- ', np.sum(arr))
print('sum(axis) -- ', np.sum(arr, axis=1))
print('sum(initial) -- ', np.sum(arr, axis=1, initial=2))