import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# vertical stacking
print("Vertical stacking:\n", np.vstack((a, b)))

# horizontal stacking
print("\nHorizontal stacking:\n", np.hstack((a, b)))

c = [5, 6]

# stacking columns
print("\nColumn stacking:\n", np.column_stack((a, c)))

# concatenation method
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))

print(np.arange('2017-02', '2017-03', dtype='datetime64[D]'))


A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

print("\nRank of A:", np.linalg.matrix_rank(A))
print("\nTrace of A:", np.trace(A))
print("\nDeterminant of A:", np.linalg.det(A))
print("\nInverse of A:\n", np.linalg.inv(A))
print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))


# x + 2*y = 8
# 3*x + 4*y = 18

# coefficients
a = np.array([[1, 2], [3, 4]])
# constants
b = np.array([8, 18])
print("Solution of linear equations:", np.linalg.solve(a, b))
