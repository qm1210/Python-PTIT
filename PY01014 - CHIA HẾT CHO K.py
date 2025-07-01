from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

if __name__ == '__main__':
    a, k, n = map(int, input().split())
    start = n - a
    res = []
    mark = 0
    start = (k - a % k) % k
    if start == 0:
        start = k
    for i in range(start, n - a + 1, k):
        res.append(i)
    if res:
        print(*res)
    else:
        print("-1")