from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *
from heapq import *

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n, p = map(int, input().split())
        x = 0
        tmp = 1
        while p ** tmp <= n:
            x += n // (p ** tmp)
            tmp += 1
        print(x)
        