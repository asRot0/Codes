import numpy as np

mat = np.matrix([[1, 2, 3],
                 [2, 3, 4]])
print(type(mat), mat, sep='\n')
print(mat.reshape((3, 2)))
mat.resize((1, 6))
print(mat, mat.shape)

# creating an array of 6 dimension
# using ndmin
arr = np.array([2, 4, 6, 8, 10], ndmin=6)
print(arr, arr.shape)

arr = np.arange(9)
print(arr, type(arr))

print(np.resize(arr, (5,5)))

arr.resize(5,5)
print(arr)
