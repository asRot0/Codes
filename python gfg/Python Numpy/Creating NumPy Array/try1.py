import numpy as np

print(np.eye(4,5))
print(np.eye(4,5, k=-1))

arr = np.zeros((2,), dtype=[('x', float), ('y', int), ('z', complex)])
print(arr)
