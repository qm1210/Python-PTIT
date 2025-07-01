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
        n, k = map(int, input().split())
        s = input()
        pos = []
        for i in range(n):
            if s[i] == "1":
                pos.append(i)
        cnt = 0
        r = 0
        for i in range(len(pos)):
            while r < len(pos) and abs(pos[r] - pos[i]) <= k:
                r += 1
            cnt += 2 * (r - i - 1) + 1
        if cnt == 0:
            print("0/1")
        else:
            total = n * n
            g = gcd(cnt, total)
            print(f"{cnt // g}/{total // g}")