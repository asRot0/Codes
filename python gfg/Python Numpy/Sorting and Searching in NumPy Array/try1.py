import numpy as np

arr = np.array([10, 32, 30, 50, 20, 82, 91, 45])

print("arr = {}".format(arr))

i = np.where(arr == 30)
print("i = {}".format(i))
print("idx of element 30 is ", i[0])

arr = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6]
print("arr = {}".format(arr))

print("left-most index = {}".format(np.searchsorted(arr, 3, side="left")))
print("right-most index = {}".format(np.searchsorted(arr, 3, side="right")))
