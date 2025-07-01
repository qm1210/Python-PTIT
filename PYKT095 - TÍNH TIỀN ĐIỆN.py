from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class GiaDinh:
    cnt = 1
    def __init__(self, ten, loai, dau, cuoi):
        self.ten = self.chuanHoa(ten)
        self.loai = loai
        self.dau = dau
        self.cuoi = cuoi
        self.dien = self.cuoi - self.dau
        self.vuot = 0
        self.vat = 0
        if self.loai == "A":
            self.muc = 100
        elif self.loai == "B":
            self.muc = 500
        else:
            self.muc = 200
        if self.dien <= self.muc:
            self.tien = 450 * self.dien
            self.total = self.tien
        else:
            self.tien = 450 * self.muc
            self.vuot = (self.dien - self.muc) * 1000
            self.vat = self.vuot // 20
            self.total = self.tien + self.vuot + self.vat
        self.ma = f"KH{GiaDinh.cnt:02d}"
        GiaDinh.cnt += 1
    
    def chuanHoa(self, ten):
        tmp = ""
        a = ten.split()
        for x in a:
            tmp += x.capitalize() + " "
        return tmp.strip()
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.tien} {self.vuot} {self.vat} {self.total}"

def cmp(a, b):
    if a.total < b.total:
        return 1
    else:
        return -1

if __name__ == '__main__':
    t = int(input())
    arr = []
    while t > 0:
        t -= 1
        ten = input().strip()
        loai, dau, cuoi = input().split()
        gd = GiaDinh(ten, loai, int(dau), int(cuoi))
        arr.append(gd)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)




