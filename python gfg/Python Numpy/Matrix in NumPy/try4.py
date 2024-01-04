import numpy as np

arr = np.matrix('[4, 1; 12, 3]')

print(arr, type(arr))
print(arr.var(), 'variance')
print(arr.transpose(), 'transpose')

arr1 = np.array(((4, 1), (12, 3)))
print(arr1, type(arr1))
print(arr1.var(), 'variance')

arr2 = np.array([[1, 2], [5, 6]])
print(arr2, type(arr2))
inverse_array = np.linalg.inv(arr2)
print(inverse_array, 'inverse')
