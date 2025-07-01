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
        n, m = map(int, input().split())
        a = []
        for i in range(n):
            row = list(map(int, input().split()))
            a.append(row)
        k = []
        total = 0
        for i in range(3):
            row = list(map(int, input().split()))
            k.append(row)
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                for u in range(-1, 2):
                    for v in range(-1, 2):
                        total += a[i + u][j + v] * k[u + 1][v + 1]
        print(total)