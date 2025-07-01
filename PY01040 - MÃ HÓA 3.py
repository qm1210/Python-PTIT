from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

def check(s):
    return s[0] != '0'

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        l = len(s)
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s1 = s[:l // 2]
        s2 = s[l // 2:]
        total1, total2 = 0, 0
        new1, new2 = "", ""
        for c in s1:
            total1 += ord(c) - ord("A")
        for c in s1:
            new1 += alpha[(alpha.index(c) + total1) % 26]
        for c in s2:
            total2 += ord(c) - ord("A")
        for c in s2:
            new2 += alpha[(alpha.index(c) + total2) % 26]
        res = ""
        for i in range(len(new1)):
            res += alpha[(alpha.index(new1[i]) + (ord(new2[i]) - ord("A"))) % 26]
        print(res)
        