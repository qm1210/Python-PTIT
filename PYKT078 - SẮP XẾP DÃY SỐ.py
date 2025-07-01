from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        idx = a.index(max(a))
        a = a[:idx] + [m] + a[idx:]
        res = []
        for i in range(len(a)):
            if a[i] < 0:
                res.append(a[i])
        for i in range(len(a)):
            if a[i] >= 0:
                res.append(a[i])
        print(*res)