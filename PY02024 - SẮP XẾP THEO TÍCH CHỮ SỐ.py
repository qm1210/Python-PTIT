from functools import cmp_to_key
from math import *

def tich(n):
    total = 1
    while n != 0:
        m = n % 10
        n //= 10
        total *= m
    return total

def cmp(a, b):
    if tich(a) != tich(b):
        return tich(a) - tich(b)
    else:
        return a - b
    

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(key=cmp_to_key(cmp))
        print(" ".join(map(str, a)))