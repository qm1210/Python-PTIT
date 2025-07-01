from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    f = open("DATA.in", "r")
    a = f.read().split()
    res = []
    for x in a:
        if not x.isdigit() or int(x) > 10 ** 18:
            res.append(x)
    res.sort()
    print(*res)