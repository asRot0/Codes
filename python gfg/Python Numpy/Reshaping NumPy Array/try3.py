import numpy as np

arr = np.array([[2, 3], [4, 5]])

# using array.flatten() method
flat_arr = arr.flatten(order='F')
print(flat_arr)

mat = np.matrix([[1, 2], [2, 3], [3, 4]])
# applying matrix.ravel() method
flat_mat = mat.ravel()
print(flat_mat)
