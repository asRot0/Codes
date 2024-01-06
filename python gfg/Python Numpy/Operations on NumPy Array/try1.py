# Python program explaining

import numpy as np

num1 = 10
num2 = 11
print('num1: ', num1, '\nnum2: ', num2)
print("bitwise_and of 10 and 11 : ", np.bitwise_and(num1, num2))
print("bitwise_or 10 and 11 : ", np.bitwise_or(num1, num2))
print("bitwise_xor of 10 and 11 : ", np.bitwise_xor(num1, num2))
print("inversion of 10 : ", np.invert(num1))
print("bitwise_not of 10 : ", np.bitwise_not(num1))
print('- '*20)

a = [2, 8, 125]
b = [3, 3, 115]
print('a: ', a, '\nb: ', b)
print("Output array after bitwise_and: ", np.bitwise_and(a, b))
print("Output array after bitwise_or: ", np.bitwise_or(a, b))
print("Output array after bitwise_xor: ", np.bitwise_xor(a, b))
print("Output array after inversion: ", np.invert(a))
print('- '*20)

'''
this operation is equivalent to multiplying arr1 by 2**arr2. 
For example, if the number is 5 and we want to 2 bit left shift then 
after left shift 2 bit the result will be 5*(2^2) = 20
'''
in_num = 5
bit_shift = 2
print("Input  number : ", in_num)
print("Number of bit shift : ", bit_shift)
out_num = np.left_shift(in_num, bit_shift)
print("After left shifting 2 bit  : ", out_num)
print('- '*20)

'''
this operation is equivalent to dividing arr1 by 2**arr2. 
For example, if the number is 20 and we want to 2-bit right shift then
 after right shift 2-bit the result will be 20/(2^2) = 5
'''
in_num = 20
bit_shift = 2
print("Input  number : ", in_num)
print("Number of bit shift : ", bit_shift)
out_num = np.right_shift(in_num, bit_shift)
print("After right shifting 2 bit  : ", out_num)
print('- '*20)

in_num = 10
print("Input  number : ", in_num)
out_num = np.binary_repr(in_num)
print("binary representation of 10 : ", out_num)

in_arr = [5, -8]

print("Input array : ", in_arr)

# binary representation of first array
# element without using width parameter
out_num = np.binary_repr(in_arr[0])
print("Binary representation of 5")
print("Without using width parameter : ", out_num)

# binary representation of first array
# element using width parameter
out_num = np.binary_repr(in_arr[0], width=5)
print("Using width parameter: ", out_num)

print("\nBinary representation of -8")

# binary representation of 2nd array
# element without using width parameter
out_num = np.binary_repr(in_arr[1])
print("Without using width parameter : ", out_num)

# binary representation of 2nd array
# element  using width parameter
out_num = np.binary_repr(in_arr[1], width=5)
print("Using width parameter : ", out_num)
print('- '*20)

a = np.array([[[1, 0, 1],
               [0, 1, 0]],
              [[1, 1, 0],
               [0, 0, 1]]])
# packing elements of an array
# using packbits() function
b = np.packbits(a, axis=-1)
print(b)

a = np.array([[2], [7], [23]], dtype=np.uint8)
# packing elements of an array
# using unpackbits() function
b = np.unpackbits(a, axis=1)
print(b)