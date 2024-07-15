#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    factors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    print(max(factors, key=lambda x: sum(map(int, str(x)))))
