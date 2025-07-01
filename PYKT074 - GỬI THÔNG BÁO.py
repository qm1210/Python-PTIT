from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *
from heapq import *

def rotate(s, n):
    return s[n:] + s[:n]

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        res = ""
        a = s.split()
        for x in a:
            if len(res + " " + x) <= 100:
                if not res:
                    res += x
                else:
                    res += " " + x
            else:
                break
        print(res)
