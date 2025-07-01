from math import *
from collections import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        cnt = 0
        min_val = min(a)
        max_val = max(a)
        for i in range(min_val, max_val + 1):
            if i not in a:
                cnt += 1
        print(cnt)