from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class CaThi:
    cnt = 1
    def __init__(self, ngay, gio, phong):
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.ma = "C" + f"{CaThi.cnt:03d}"
        CaThi.cnt += 1
    
    def __str__(self):
        return f"{self.ma} {self.ngay} {self.gio} {self.phong}" 

def cmp(a, b):
    if a.ngay < b.ngay:
        return -1
    elif a.ngay > b.ngay:
        return 1
    else:
        if a.gio < b.gio:
            return -1
        else:
            return 1

if __name__ == '__main__':
    f = open('CATHI.in', 'r')
    t = int(f.readline())
    arr = []
    while t > 0:
        t -= 1
        ngay = f.readline().strip()
        gio = f.readline().strip()
        phong = f.readline().strip()
        ct = CaThi(ngay, gio, phong)
        arr.append(ct) 
    arr.sort(key=cmp_to_key(cmp))   
    for x in arr:
        print(x)
        

