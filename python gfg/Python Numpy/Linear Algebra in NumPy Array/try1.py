import numpy as np

A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))

# Trace of matrix A
print("\nTrace of A:", np.trace(A))

# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))

# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))

print("\nMatrix A raised to power 3:\n",
      np.linalg.matrix_power(A, 3))

arr = np.array([[1, -2j], [2j, 5]])
print('array -- ', arr)

# eigen value and eigen vector
c, d = np.linalg.eigh(arr)
print('eigen value -- ', c)
print('eigen vector -- ', d)

arr = np.diag((1, 2, 3))
print('array -- ', arr)

c, d = np.linalg.eig(arr)
print('eigen value -- ', c)
print('eigen vector -- ', d)

m = np.array([[1, 2, 3],
              [2, 3, 4],
              [4, 5, 6]])

print("Printing the Original square array:\n", m)

# eigenvalues and eigenvectors
w, v = np.linalg.eig(m)

# printing eigen values
print("Printing the Eigen values of the given square array:\n", w)

# printing eigen vectors
print("Printing Right eigenvectors of the given square array:\n", v)
