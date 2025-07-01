from functools import cmp_to_key
from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        dd = [0] * 1001
        n = int(input())
        while n > 0:
            n -= 1
            m = int(input())
            dd[m] += 1
        index = dd.index(max(dd))
        print(index)
