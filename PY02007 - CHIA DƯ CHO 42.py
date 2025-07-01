from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys
from heapq import *

if __name__ == '__main__':
    a = []
    while True:
        try:
            s = input()
            if s == "":
                continue
            tmp = s.split()
            for x in tmp:
                a.append(x)
        except EOFError:
            break
    for i in range(len(a)):
        a[i] = int(a[i]) % 42
    se = set(a)
    print(len(se))