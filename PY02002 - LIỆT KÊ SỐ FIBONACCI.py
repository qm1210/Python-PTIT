from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

if __name__ == '__main__':
    t = int(input())
    f = [0] * 93
    f[1] = f[2] = 1
    for i in range(3, 93):
        f[i] = f[i - 1] + f[i - 2]
    while t > 0:
        t -= 1
        res = []
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            res.append(f[i])
        print(" ".join(map(str, res)))
