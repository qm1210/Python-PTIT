from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    n = int(input())
    a = []
    res = [0] * n
    for i in range(n):
        a.append(list(map(int, input().split())))
    if n == 2:
        res = [a[0][1] // 2, a[0][1] // 2]
    else:
        res[0] = (a[0][1] + a[0][2] - a[1][2]) // 2
        for i in range(1, n):
            res[i] = a[0][i] - res[0]
    print(*res)
