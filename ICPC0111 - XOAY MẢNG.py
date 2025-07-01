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
        n, d = map(int, input().split())
        a = list(map(int, input().split()))
        res = a[d:] + a[:d]
        print(*res)

