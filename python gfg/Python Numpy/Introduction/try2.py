# Python program to demonstrate
# indexing in numpy
import numpy as np

# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Slicing array
temp = arr[:2, ::2]
print("Array with first 2 rows and alternate"
      "columns(0 and 2):\n", temp)

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("\nElements at indices (0, 3), (1, 2), (2, 1),"
      "(3, 0):\n", temp)

# boolean array indexing example
cond = arr > 0  # cond is a boolean array
temp = arr[cond]
print("\nElements greater than 0:\n", temp)

print(arr + 1, arr - 1, arr * 10, arr ** 2, sep='\n')
arr *= 10
print(arr, arr.T, sep='\n')

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
print(arr.max(), arr.max(axis=0), arr.max(axis=1))
print(arr.sum(), arr.sum(axis=0), arr.sum(axis=1, dtype=float))
print(arr.cumsum(), arr.cumsum(axis=0), arr.cumsum(axis=1), sep='\n')
