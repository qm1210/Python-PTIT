from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

def check(n):
    s = str(n)
    total = 0
    for c in s:
        total += factorial(int(c))
    if total == n:
        return True
    else:
        return False

if __name__ == '__main__':
    t = int(input())
    while t > 0:  
        t -= 1
        n = int(input())
        if check(n):
            print("Yes")
        else:
            print("No")