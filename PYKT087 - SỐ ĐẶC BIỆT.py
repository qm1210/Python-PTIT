from math import *
from collections import *
import re
import sys

def power_mod(a, b, m):
    res = 1
    a = a % m  
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

if __name__ == '__main__':
    t = int(input())
    mod = 10**9 + 7
    while t > 0:
        t -= 1
        n, m = map(int, input().split())
        s = ""
        res = 0
        while m > 0:
            s += str(m % 2)
            m //= 2
        for i in range(len(s)):
            if s[i] == '1':
                power = power_mod(n, i, mod)
                res = (res + power) % mod
        print(res)