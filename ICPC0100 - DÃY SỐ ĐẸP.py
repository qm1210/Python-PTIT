from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        cnt = 0
        a = list(map(int, input().split()))
        for i in range(n - 1):
            small = min(a[i], a[i + 1])
            large = max(a[i], a[i + 1])
            while small * 2 < large:
                cnt += 1
                small *= 2
        print(cnt)
            