from functools import cmp_to_key
from math import *

def tong(n):
    sum = 0
    while n != 0:
        m = n % 10
        n //= 10
        sum += m
    return sum

def cmp(a, b):
    sum = 0
    if tong(a) != tong(b):
        return tong(a) - tong(b)
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