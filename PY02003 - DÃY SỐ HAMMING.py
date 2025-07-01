from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys
from heapq import *

limit = 10 ** 18 + 1

if __name__ == '__main__':
    t = int(input())
    hamming = []
    seen = set()
    h = [1]
    while h:
        x = heappop(h)
        if x not in seen:
            hamming.append(x)
            seen.add(x)
            if x * 2 <= limit:
                heappush(h, x * 2)
            if x * 3 <= limit:
                heappush(h, x * 3)
            if x * 5 <= limit:
                heappush(h, x * 5)
    mp = {v: i + 1 for i, v in enumerate(hamming)}
    while t > 0:
        t -= 1
        n = int(input())
        print(mp.get(n, "Not in sequence"))