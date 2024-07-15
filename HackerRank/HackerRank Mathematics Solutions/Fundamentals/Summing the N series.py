#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'summingSeries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.


# sum of the arithmetic series formula sum = no of (terms/2) * (first term + last term)
# simplified the Tn = n^2 - (n-1)^2 = 2n-1
# sum = (n/2) * (1 + 2n-1) = n^2


def summingSeries(n):
# Write your code here
    res = n * n
    return res % (10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
