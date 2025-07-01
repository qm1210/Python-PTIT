from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        a = []
        n, m = map(int, input().split())
        for i in range(n):
            a.append(list(map(int, input().split())))
        b = []
        c = []
        for j in range(m):
            row = []
            for i in range(n):
                row.append(a[i][j])
            b.append(row)
        for i in range(n):
            row = []
            for j in range(n):
                s = 0
                for k in range(m):
                    s += a[i][k] * a[j][k]
                row.append(s)
            c.append(row)
        for x in c:
            print(" ".join(map(str, x)))
                