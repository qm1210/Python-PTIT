from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == "__main__":
    n, q = map(int, input().split())
    diff = [0] * (n + 2)
    while q > 0:
        q -= 1
        x, y = map(int, input().split())
        diff[x] += 1
        diff[y + 1] -= 1
    res = []
    prefix = 0
    for i in range(1, n + 1):
        prefix += diff[i]
        bit = prefix % 2
        res.append(str(bit))
    print(*res)