#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    def __init__(self, items, coins):
        self.items = items
        self.coins = coins

    def buy(self, req_items, money):
        if(self.items>=req_items and req_items*self.coins<=money):
            self.items -= req_items
            return money - (req_items*self.coins)
        else:
            return 'Not enough items in the machine' if self.items<req_items else 'Not enough coins'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
