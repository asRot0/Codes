import numpy as np

arr = np.array([[10, 22], [13, 6]])
q, r = np.linalg.qr(arr)  # find the QR factor of array

print("Decomposition of matrix (2x2):")
print("q=\n", q, "\nr=\n", r)
print("__ " * 20)

arr = np.array([[0, 1], [1, 0], [1, 1], [2, 2]])
q, r = np.linalg.qr(arr)

print("Decomposition of matrix (2x4):")
print("q=\n", q, "\nr=\n", r)
print("__ " * 20)

arr = np.array([[5, 11, -15], [12, 34, -51],
                [-24, -43, 92]], dtype=np.int32)
q, r = np.linalg.qr(arr)

print("Decomposition of matrix (3x3):")
print("q=\n", q, "\nr=\n", r)
