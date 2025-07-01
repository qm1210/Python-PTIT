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
    if a == 0 or b == 0 or c == 0:
        return False
    if a > b or b > c:
        return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        n = input()
        l = len(n)
        cnt = 0
        i = 0
        while i <= len(s) - l:
            if s[i:i+l] == n:
                cnt += 1
                i += l
            else:
                i += 1
        print(cnt)