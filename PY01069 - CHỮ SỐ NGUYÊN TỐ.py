from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

def check(s):
    if int(s) % 2 == 0:
        return False
    if "2" not in s or "3" not in s or "5" not in s or "7" not in s:
        return False
    return True

if __name__ == "__main__":
    n = int(input())
    a = [2, 3, 5, 7]
    res = []
    for i in range(4, n + 1):
        prods = list(product(a, repeat=i))
        for p in prods:
            res.append("".join(map(str, p)))
    for x in res:
        if check(x):
            print(x)
        