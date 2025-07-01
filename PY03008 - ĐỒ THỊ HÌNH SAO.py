from math import *
import sys
from itertools import combinations
import re
from functools import cmp_to_key

if __name__ == '__main__':
    n = int(input())
    t = n - 1
    deg = [0] * n
    check = True
    while t > 0:
        t -= 1
        u, v = map(int, input().split())
        deg[u - 1] += 1
        deg[v - 1] += 1
    cnt1, cnt2 = 0, 0
    cnt1 = deg.count(n - 1)
    cnt2 = deg.count(1)
    if cnt1 == 1 and cnt2 == n - 1:
        print("Yes")
    else:
        print("No")