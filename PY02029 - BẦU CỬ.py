from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == "__main__":
    n , m = map(int, input().split())
    a = list(map(int, input().split()))
    mp = {}
    mark = 0
    check = True
    for i in range(n):
        if a[i] not in mp:
            mp[a[i]] = 1
        else:
            mp[a[i]] += 1
    c = list(mp.values())
    c.sort()
    if len(c) == 1:
        check = False
    else:
        max_val = max(c)
        for i in range(len(c) - 1, -1, -1):
            if c[i] != max_val:
                mark = c[i]
                break
            if c[i] == max_val and i == 0:
                check = False
                break
        for i in range(n):
            if mp[a[i]] == mark:
                mark = a[i]
                break
    if check:
        print(mark)
    else:
        print("NONE")