import numpy as np

matrix = np.array([[33, 55, 66, 74], [23, 45, 65, 27],
                  [87, 96, 34, 54]])

print('matrix -- ', matrix)
sd = np.std(matrix)
print('standard deviation -- ', sd)

arr1 = [120, 24, 42, 10]
arr2 = [2250, 12, 20, 50]

print('arr1 -- ', arr1)
print('arr2 -- ', arr2)

print('GCD of arr1 and arr2 -- ', np.gcd(arr1, arr2))