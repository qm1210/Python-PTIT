from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

def check(s):
    if len(s) < 3:
        return False
    peak = max(s)
    idx = s.index(peak)
    for i in range(idx - 1):
        if s[i] >= s[i + 1]:
            return False
    for i in range(idx + 1, len(s) - 1):
        if s[i] <= s[i + 1]:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")