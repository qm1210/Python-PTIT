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
        n, c, d = map(int, input().split())
        a = []
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        arr1 = a[:c]
        arr2 = a[c:c+d]
        res1 = (sum(arr1) / c) + (sum(arr2) / d)
        arr3 = a[:d]
        arr4 = a[d:d+c]
        res2 = (sum(arr3) / d) + (sum(arr4) / c)
        res = max(res1, res2)
        print(f"{res:.6f}")