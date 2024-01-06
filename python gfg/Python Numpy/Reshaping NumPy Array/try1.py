import numpy as np

# creating a numpy array
array = np.arange(1, 17)
# printing array
print("Array : " + str(array))
# length of array
n = array.size
# N-D array N dimension
N = 4
# calculating M
M = n // N

# reshaping numpy array
# converting it to 2-D from 1-D array
reshaped = array.reshape((N, M))
# printing reshaped array
print("First Reshaped Array : ")
print(reshaped)
# creating another reshaped array
reshaped = np.reshape(array, (2, 8))
# printing reshaped array
print("Second Reshaped Array : ")
print(reshaped)

# reshaping numpy array
# converting it to 3-D from 1-D array
reshaped = array.reshape((2, 2, 4))
print("Reshaped 3D array : ")
print(reshaped)

arr = np.array([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 5]])
# converting it to 1-D from 2-D array
reshaped = arr.reshape(9)
print("Reshaped 1D array : ")
print(reshaped)

# reshaping using unknown dimension
# converting it to 3-D from 1-D array
reshaped = array.reshape((2, 2, -1))
print("Unknown First Reshaped Array : ")
print(reshaped)

# converting it to 2-D array
reshaped = array.reshape((4, -1))
print("Unknown Second Reshaped Array : ")
print(reshaped)
