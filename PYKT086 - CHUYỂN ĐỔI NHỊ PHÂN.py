from math import *
from collections import *
import re
import sys

if __name__ == '__main__':
    f = open('DATA.in', 'r')
    t = int(f.readline())
    tmp = "0123456789ABCDEF"
    while t > 0:
        t -= 1
        b = int(f.readline())
        s = f.readline().strip()
        srev = s[::-1]
        s10 = 0
        for i in range(len(srev)):
            s10 += int(srev[i]) * 2 ** i
        s = s10
        res = ""
        while s > 0:
            res += tmp[s % b]
            s //= b
        res = res[::-1]
        print(res)