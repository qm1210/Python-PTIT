from math import *
from sys import *
from itertools import *
from functools import cmp_to_key
from datetime import *
import re
import sys

if __name__ == '__main__':
    t = int(input())
    cs = "0123456789ABCDEF"
    while t > 0:  
        t -= 1
        n = int(input())
        s = input()
        s = s[::-1]
        tmp = 0
        for i in range(len(s)):
            if s[i] == "1":
                tmp += 2 ** i
        res = ""
        while tmp > 0:
            res += str(cs[tmp % n])
            tmp //= n
        res = res[::-1]
        print(res)

