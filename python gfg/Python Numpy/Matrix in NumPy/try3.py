import numpy as np

arr = np.array([[55, 25, 15],
                [30, 44, 2],
                [11, 45, 77]])
print(arr)

eg = np.linalg.eigvals(arr)
print(eg)

det = np.linalg.det(arr)
print(int(det))
