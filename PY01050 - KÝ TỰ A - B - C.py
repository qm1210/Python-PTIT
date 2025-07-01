from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

def check(s):
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    return 'A' in s and 'B' in s and 'C' in s and a <= b <= c

if __name__ == '__main__':
    n = int(input())
    for i in range(3, n + 1):
        for p in product("ABC", repeat=i):
            s = "".join(p)
            if check(s):
                print(s)