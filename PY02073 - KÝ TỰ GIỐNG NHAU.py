from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        dp = [0] * (n + 2)
        x, y, z = map(int, input().split())
        dp[1] = x
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + x
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i // 2] + z)
            else:
                dp[i] = min(dp[i], dp[(i + 1) // 2] + z + y)
        print(dp[n])