from math import *
from functools import cmp_to_key
import sys
import re

class SinhVien:
    def __init__(self, s, c, t):
        self.s = s
        self.c = c
        self.t = t
    
    def __str__(self):
        return f"{self.s} {self.c} {self.t}"

def cmp(a, b):
    if a.c > b.c:
        return -1
    elif a.c < b.c:
        return 1
    else:
        if a.t < b.t:
            return -1
        elif a.t > b.t:
            return 1
        else:
            if a.s < b.s:
                return -1
            else: 
                return 1

if __name__ == "__main__":
    n = int(input())
    arr = []
    while n > 0:
        n -= 1
        s = input()
        c, t = map(int, input().split())
        sv = SinhVien(s, c, t)
        arr.append(sv)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)
