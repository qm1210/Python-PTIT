from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *
from heapq import *

class pair:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        arr = []
        cnt = 0
        end = -1
        while n > 0:
            n -= 1
            a, b = map(int, input().split())
            arr.append(pair(a, b))
        arr.sort(key=lambda x: (x.x2, x.x1))
        for x in arr:
            if x.x1 >= end:
                cnt += 1
                end = x.x2
        print(cnt)