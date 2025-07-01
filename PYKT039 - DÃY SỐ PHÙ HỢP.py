from decimal import Decimal
from functools import cmp_to_key
from math import *

def check(a, b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if check(a, b):
            print("YES")
        else:
            print("NO")

