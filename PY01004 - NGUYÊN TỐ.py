from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:  
        t -= 1
        n = int(input())
        cnt = 0
        for k in range(n):
            if gcd(k, n) == 1:
                cnt += 1
        if nt(cnt):
            print("YES")
        else:
            print("NO")