from decimal import Decimal
from functools import cmp_to_key
from math import *

def cmp(a, b):
    if a.avg < b.avg:
        return 1
    elif a.avg > b.avg:
        return -1
    else:
        if a.ma < b.ma:
            return -1
        else:
            return 1

class HocSinh:
    cnt = 1
    def __init__(self, ten, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10):
        self.ma = "HS" + format(self.cnt, "02d")
        HocSinh.cnt += 1
        self.ten = ten
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7 
        self.d8 = d8
        self.d9 = d9
        self.d10 = d10
        self.avg = (d1 * 2 + d2 * 2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10) / 10 / 1.2
        if self.avg < 5:
            self.danhgia = "YEU"
        elif self.avg <= 6.9:
            self.danhgia = "TB"
        elif self.avg <= 7.9:
            self.danhgia = "KHA"
        elif self.avg <= 8.9:
            self.danhgia = "GIOI"
        else:
            self.danhgia = "XUAT SAC"
        
    def __str__(self):
        return self.ma + " " + self.ten + " " + f"{self.avg:.1f}" + " " + self.danhgia 

        
if __name__ == '__main__':
    t = int(input())
    res = []
    while t > 0:
        t -= 1
        ten = input()
        d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = map(float, input().split())
        hs = HocSinh(ten, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)
        res.append(hs)
    res.sort(key = cmp_to_key(cmp))
    for i in res:
        print(i)
