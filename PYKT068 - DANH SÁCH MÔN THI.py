from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class MonThi:
    def __init__(self, ma, ten, hinhThuc):
        self.ma = ma
        self.ten = ten
        self.hinhThuc = hinhThuc
        
    def __str__(self):
        return f"{self.ma} {self.ten} {self.hinhThuc}"

def cmp(a, b):
    if a.ma < b.ma:
        return -1
    else:
        return 1

if __name__ == '__main__':
    t = int(input())
    arr = []
    while t > 0:
        t -= 1
        ma = input().strip()
        ten = input().strip()
        hinhThuc = input().strip()
        mt = MonThi(ma, ten, hinhThuc)
        arr.append(mt)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)