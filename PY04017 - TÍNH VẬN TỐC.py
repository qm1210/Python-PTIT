from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class ThiSinh:
    def __init__(self, ten, dv, den):
        self.ten = ten
        self.dv = dv
        self.den = den
        self.timeden = datetime.strptime(den, "%H:%M")
        self.timedi = datetime.strptime("6:00", "%H:%M")
        self.tg = (self.timeden - self.timedi).seconds / 3600
        a = dv.split()
        b = ten.split()
        self.ma = ""
        for i in range(len(a)):
            self.ma += a[i][0]
        for i in range(len(b)):
            self.ma += b[i][0]
        self.vt = round(120 / self.tg)
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.dv} {self.vt} Km/h" 

def cmp(a, b):
    if a.den < b.den:
        return -1
    else:
        return 1

if __name__ == "__main__":
    t = int(input())
    arr = []
    while t > 0:
        t -= 1
        ten = input().strip()
        dv = input().strip()
        den = input().strip()
        arr.append(ThiSinh(ten, dv, den))
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)