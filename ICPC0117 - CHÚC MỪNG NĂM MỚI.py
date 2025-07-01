from math import *
import sys
from itertools import combinations
import re
from functools import cmp_to_key

if __name__ == '__main__':
    t = int(input())
    se = set()
    while t > 0:
        t -= 1
        s = input()
        se.add(s)
    print(len(se))

