from math import *
import sys
from itertools import combinations
import re
from functools import cmp_to_key

def cmp(a, b):
    if mp[a] < mp[b]:
        return 1
    elif mp[a] > mp[b]:
        return -1
    else:
        if a > b:
            return 1
        else:
            return -1

if __name__ == '__main__':
    t = int(input())
    vb = ""
    while t > 0:
        t -= 1
        vb += input().lower() + " "
    a = re.split(r'[^a-z]+', vb)
    mp = {}
    for x in a:
        if x == "":
            continue
        if x in mp:
            mp[x] += 1
        else:
            mp[x] = 1
    res = list(mp.keys())
    res.sort(key=cmp_to_key(cmp))
    for x in res:
        print(x, mp[x], sep=" ")

