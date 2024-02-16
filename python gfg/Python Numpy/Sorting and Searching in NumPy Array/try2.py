import numpy as np

arr = np.array([[12, 15], [16, 11], [8, 10]])
print(arr, '--arr')

arr1 = np.sort(arr, axis=0)
print(arr1, '--sorted arr along axis 0')

arr2 = np.sort(arr, axis=1)  # axis=-1
print(arr2, '--sorted arr along axis 1')

arr3 = np.sort(arr, axis=None)
print(arr3, '--sorted arr along none axis')
print('__ '*10)

a = np.array([12, 15, 10, 11])
print('arr a --', a, id(a))
a.sort()
print('arr a (in-place sort) --', a, id(a))
print('__ '*10)
