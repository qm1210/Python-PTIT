from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

def check(s):
    if s != s[::-1]:
        return False
    return True

if __name__ == "__main__":
    f = open("VANBAN.in", "r")
    a = f.read().split()
    mp = {}
    max_len = 0
    res = []
    for x in a:
        if check(x) and len(x) > max_len:
            max_len = len(x)
            res.clear()
            mp.clear()
            if x not in res:
                res.append(x)
            if x not in mp:
                mp[x] = 1
            else:
                mp[x] += 1
        elif check(x) and len(x) == max_len:
            if x not in res:
                res.append(x)
            if x not in mp:
                mp[x] = 1
            else:
                mp[x] += 1
    for x in res:
        print(x, mp[x], sep=" ")