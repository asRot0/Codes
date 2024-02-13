#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    """
       Using The loop method: This method works by looping through the array, starting from the first element, and
       swapping each element with the element before it

       for i in range(n):
           temp = arr[0]
           for j in range(1, len(arr)):
               arr[j - 1] = arr[j]
           arr[-1] = temp
       return arr


    Using the collections.deque class: The collections.deque class is a data structure that can be used to
    implement a queue. The rotate() method of the collections.deque class can be used to rotate the elements
    of the deque

    from collections import deque

    rotated_array = deque(arr)
    return rotated_array.rotate(-d)


    Using the numpy.roll() function: The numpy.roll() function can be used to rotate the elements of an array
    import numpy as np

    return np.roll(arr, d)
    """

    # Using the slice operator: The slice operator can be used to slice the array and then reassign
    # the elements to the array

    return arr[d:] + arr[:d]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
