import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr, type(arr), arr.ndim, arr.shape, arr.size, arr.dtype)

arr2 = np.array(((1, 2, 3), (1, 3, 5)), dtype=float)
print(arr2)

print(np.zeros((3,4)))
print(np.full((3,3), 6, dtype=complex))
print(np.random.random((2,3)))

print(np.arange(1, 10, 2, dtype=float))
print(np.arange(10).reshape(2, 5))
print(np.linspace(1, 10, 5))

arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
print(arr, arr.reshape(2, 3, 2), sep='\n')
print(arr.flatten(), arr.flatten(order='F'))
