import numpy as np

a = np.arange(10, 1, -2)
print("A sequential array with a negative step: ", a)
newarr = a[np.array([3, 1, -1])]
print("Elements at these indices are: ", newarr)
print('- ' * 20)

arr = np.arange(20)
print('arr is -- ', arr)
print('a[-10: 18: 2] -- ', arr[-10: 18: 2])
print('a[15:] -- ', arr[15:])
print('- ' * 20)

# 3D dimensional array
b = np.array([[[1, 2, 3], [4, 5, 6]],
              [[7, 8, 9], [10, 11, 12]]])
print('3D arr -- \n', b)
print('b[...,-1] -- \n', b[..., -1])  # b[: ,: ,-1]
print('- ' * 20)

# first dimension is paired with the element
# of the second dimension
c = np.array([[1, 2], [3, 4], [5, 6]])
print('c arr -- \n', c)
print('purely integer indexing -- ', c[[0, 1, 2], [0, 0, 1]])
d = np.array([11, 12, 13, 14, 15, 16, 17])
print('d arr -- ', d)
print('boolean indexing -- ', d[d > 15])
sumrow = c.sum(1)
print('sumrow -- ', sumrow)
print(c[sumrow % 3 == 0])
