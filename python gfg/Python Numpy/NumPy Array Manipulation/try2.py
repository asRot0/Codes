import numpy as np

arr = np.array(((1, 2, 3), (4, 5, 6)))
arr2 = np.array(((7, 8, 9), (5, 6, 7)))

print(np.hstack((arr, arr2)))

a = np.array((1, 2, 3, 4))
b = np.array((5, 6, 7, 8))
print(np.stack((a, b), axis=1))

x = np.array([[1, 2, 3],
              [4, 5, 6]])

y = np.array([[7, 8, 9],
              [10, 11, 12]])
print(np.stack((x, y), axis=1))

block_1 = np.array([[1, 1], [1, 1]])
block_2 = np.array([[2, 2, 2], [2, 2, 2]])
block_3 = np.array([[3, 3], [3, 3], [3, 3]])
block_4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])

block_new = np.block([
    [block_1, block_2],
    [block_3, block_4]
])

print(block_new)
