from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == "__main__":
    t = int(input())
    cnt = 1
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        max_left = [0] * n
        min_right = [0] * n
        res = []
        max_left[0] = -1
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], a[i - 1])
        min_right[n - 1] = 10 ** 18
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], a[i + 1])
        for i in range(n):
            if a[i] >= max_left[i] and a[i] < min_right[i]:
                res.append(a[i])
        print(len(res))
