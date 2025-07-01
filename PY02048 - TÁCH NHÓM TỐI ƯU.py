from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = []
    tmp = [a[0]]
    for i in range(1, n):
        if abs(a[i] - a[i - 1]) <= k:
            tmp.append(a[i])
        else:
            res.append(tmp)
            tmp = [a[i]]
    res.append(tmp)
    print(len(res))