import numpy as np

vactor1 = 2 + 3j
vactor2 = 4 + 5j

dotprd = np.dot(vactor1, vactor2)
print('dot product -- ', dotprd)
print('dot product(vdot) -- ', np.vdot(vactor1, vactor2))

a = np.array([[1, 2], [3, 4]])
b = np.array([8, 18])

print('solution of linear equation -- ', np.linalg.solve(a, b))
