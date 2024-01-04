# Python program to demonstrate
# binary operators in Numpy
import numpy as np

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[4, 3],
              [2, 1]])

# add arrays
print("Array sum:\n", a + b)

# multiply arrays (elementwise multiplication)
print("Array multiplication:\n", a * b)

# matrix multiplication
print("Matrix multiplication:\n", a.dot(b))

print(np.add(a, b), np.subtract(a,b), np.multiply(a,b), np.divide(a,b), sep='\n')

# create an array of sine values
a = np.array([0, np.pi / 2, np.pi])
print("Sine values of array elements:", np.sin(a))

# exponential values
a = np.array([0, 1, 2, 3])
print("Exponent of array elements:", np.exp(a))

# square root of array values
print("Square root of array elements:", np.sqrt(a))

a = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, 5]])

# sorted array
print("Array elements in sorted order:\n",
      np.sort(a, axis=None))

# sort array row-wise
print("Row-wise sorted array:\n",
      np.sort(a, axis=1))

# specify sort algorithm
print("Column wise sort by applying merge-sort:\n",
      np.sort(a, axis=0, kind='mergesort'))

# Example to show sorting of structured array
# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
          ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

print(values)

# Creating array
arr = np.array(values, dtype=dtypes)
print(arr)

print("\nArray sorted by names:\n",
      np.sort(arr, order='name'))

print("Array sorted by graduation year and then cgpa:\n",
      np.sort(arr, order=['grad_year', 'cgpa']))