#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        print(k * 2 + 1 if k < n // 2 else (n - k - 1) * 2)
