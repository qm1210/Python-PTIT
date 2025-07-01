from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

if __name__ == '__main__':
    vb = ""
    for line in sys.stdin:
        vb += line.strip() + " "
    a = re.split(r'[.?!]', vb)
    res = []
    for x in a:
        tmp = ""
        b = x.split()
        for i in range(len(b)):
            if b[i] == "," or b[i] == ":":
                tmp += b[i]
            else:
                tmp += " " + b[i]
        res.append(tmp.strip().capitalize())
    for x in res:
        if x != "":
            print(x)
                