from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == "__main__":
    t = int(input())
    res = []
    while t > 0:
        t -= 1
        s = input()
        a = re.findall(r'\d+', s)
        for x in a:
            x = x.lstrip('0') or '0'
            res.append(int(x))
    res.sort()
    for x in res:
        print(x)