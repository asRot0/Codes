# importing Numpy package
import numpy as np

num_1d = np.arange(5)
print("One dimensional array:")
print(num_1d)

num_2d = np.arange(10).reshape(2, 5)
print("\nTwo dimensional array:")
print(num_2d)

# Combine 1-D and 2-D arrays and display
# their elements using numpy.nditer()
for a, b in np.nditer([num_1d, num_2d]):
    print("%d:%d" % (a, b), )

an_array = np.array([[1, 2], [3, 4]])
another_array = np.array([[1, 2], [3, 4]])

comparison = an_array == another_array
print(comparison)
equal_arrays = comparison.all()
print(equal_arrays)

# code to find union of more than two arrays
# import libraries
from functools import reduce

array = reduce(np.union1d, ([1, 2, 3], [1, 3, 5],
                            [2, 4, 6], [0, 0, 0]))
print("Union ", array)
