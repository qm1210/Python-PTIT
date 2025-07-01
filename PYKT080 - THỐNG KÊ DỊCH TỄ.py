from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    mark = []
    total = 0
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        mark.append([0] * m)
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                for p in range(-1, 2):
                    for q in range(-1, 2):
                        if p == 0 and q == 0:
                            continue
                        x = i + p
                        y = j + q
                        if 0 <= x < n and 0 <= y < m and mark[x][y] == 0:
                            total += a[x][y]
                            mark[x][y] = 1
    print(total)