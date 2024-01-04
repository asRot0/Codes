import numpy as np

print(np.random.random((2, 4)))

arr = np.array([1, 2])
print(arr, arr.dtype)

arr1 = np.array([1, 2], dtype=np.int64)
print(arr1, arr1.dtype)

print("\nBool Value with axis = 0 (any) : ",
      np.any([[True, False, False], [True, True, False], [False, True, True]], axis=0))
print("\nBool Value with axis = 0 (all) : ",
      np.all([[True, True, False], [True, True, False], [False, True, True]], axis=0))
print("\nBool Value with axis = 1 (any) : ",
      np.any([[False, False, False], [True, True, False], [False, True, True]], axis=1))
print("\nBool Value with axis = 1 (all) : ",
      np.all([[False, False, False], [True, True, False], [True, True, True]], axis=1))

array = np.arange(12).reshape(3, 4)
print("Original array : \n", array)
np.place(array, array > 5, [15, 25, 35])
print("\nPutting up elements to array: \n", array)

# Python Program illustrating

# numpy.insert()

# Working on 1D
arr = np.arange(5)
print("1D arr : \n", arr)
print("Shape : ", arr.shape)

# value = 9
# index = 1
# Insertion before first index
a = np.insert(arr, 1, 9)
print("\nArray after insertion : ", a)
print("Shape : ", a.shape)

# Working on 2D array
arr = np.arange(12).reshape(3, 4)
print("\n\n2D arr : \n", arr)
print("Shape : ", arr.shape)

a = np.insert(arr, 1, 9, axis=1)
print("\nArray after insertion : \n", a)
print("Shape : ", a.shape)

# Working on 2D array
arr = np.arange(12).reshape(3, 4)
print("2D arr : \n", arr)
print("Shape : ", arr.shape)

# Working with Scalars
a = np.insert(arr, [1], [[6], [7], [9]], axis=0)
print("\nArray after insertion : \n", a)
print("Shape : ", a.shape)

# Working with Scalars
a = np.insert(arr, [1], [[8], [7], [9]], axis=1)
print("\nArray after insertion : \n", a)
print("Shape : ", a.shape)
