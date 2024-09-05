import numpy as np

arr = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
arr = np.array(arr)

print(arr, id(arr))


print(np.flipud(arr))
# Rotate the array by 90 degrees clockwise
arr = np.transpose(np.flipud(arr))

print(arr, id(arr))
