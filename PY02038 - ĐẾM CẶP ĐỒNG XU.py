from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == "__main__":
    n = int(input())
    a = []
    total = 0
    for i in range(n):
        a.append(input())
    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] == "C":
                cnt += 1
        total += cnt * (cnt - 1) // 2
    for j in range(n):
        cnt = 0
        for i in range(n):
            if a[i][j] == "C":
                cnt += 1
        total += cnt * (cnt - 1) // 2
    print(total)