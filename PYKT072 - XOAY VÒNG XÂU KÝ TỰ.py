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
    a = []
    min_step = 10 ** 9
    while t > 0:
        t -= 1
        a.append(input())
    l = len(a[0])
    for i in range(l):
        target = rotate(a[0], i)
        ok = True
        cnt = 0
        for s in a:
            found = False
            for j in range(l):
                if rotate(s, j) == target:
                    cnt += j
                    found = True
                    break
            if not found:
                ok = False
                break
        if ok:
            min_step = min(min_step, cnt)
    if min_step != 10 ** 9:
        print(min_step)
    else:
        print("-1")