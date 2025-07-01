from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(list(set(a)))
    combs = list(combinations(a, k))
    for x in combs:
        print(" ".join(map(str, x)))