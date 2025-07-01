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
        n = int(input())
        q = n
        a, b = [], []
        while q > 0:
            q -= 1
            x, y = map(float, input().split())
            a.append(x)
            b.append(y)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if a[i] > a[j] and b[i] < b[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(max(dp))