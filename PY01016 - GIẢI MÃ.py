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
        s = input()
        res = []
        for c in s:
            if not c.isdigit():
                res.append(c)
            else:
                n = int(c)
                for i in range(n - 1):
                    res.append(res[-1])
        print("".join(map(str, res)))
