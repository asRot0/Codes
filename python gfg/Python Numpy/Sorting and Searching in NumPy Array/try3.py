import numpy as np

a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = 0)
print ("Along first axis : \n", arr1)
print('__ '*10)

arr = np.arange(12).reshape(3, 4)
print(arr, '--array')

print('max element', np.argmax(arr))
print('indices (axis=0) max element', np.argmax(arr, axis=0))
print('indices (axis=1) min element', np.argmin(arr, axis=1))
print('__ '*10)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

print('Indices of elements <4')
b = np.where(a < 4)
print(b)

print("Elements which are <4")
print(a[b])
print('__ '*10)

a = np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]])
print('number of nonzero values is ', a)