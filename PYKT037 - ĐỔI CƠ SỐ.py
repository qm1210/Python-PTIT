from decimal import Decimal
from functools import cmp_to_key
from math import *

if __name__ == '__main__':
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t = int(input())
    while t > 0:
        t -= 1
        n, b = map(int, input().split())
        res = []
        while n > 0:
            res.append(digits[n % b])
            n //= b
        res.reverse()
        print("".join(res))

