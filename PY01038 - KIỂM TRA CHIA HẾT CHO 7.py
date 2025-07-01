from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        check = False
        for i in range(1000):
            if n % 7 == 0:
                check = True
                break
            n += int(str(n)[::-1])
        if check:
            print(n)
        else:
            print("-1")