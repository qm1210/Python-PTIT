from decimal import Decimal
from functools import cmp_to_key
from math import *

def cmp(a, b):
    if a.tien < b.tien:
        return 1
    else:
        return -1

class HoaDon:
    cnt = 1
    def __init__(self, ten, soCu, soMoi):
        self.id = "KH" + f"{HoaDon.cnt:02d}"
        HoaDon.cnt += 1
        self.ten = ten
        self.soCu = soCu
        self.soMoi = soMoi
        self.soDien = soMoi - soCu
        if self.soDien <= 50:
            self.tien = self.soDien * 100
            self.tong = self.tien * 1.02
        elif self.soDien <= 100:
            self.tien = 50 * 100 + (self.soDien - 50) * 150
            self.tong = self.tien * 1.03
        else:
            self.tien = 50 * 100 + 50 * 150 + (self.soDien - 100) * 200
            self.tong = self.tien * 1.05
        self.tong = int(round(self.tong))
        
    def __str__(self):
        return self.id + " " + self.ten + " " + str(self.tong)

if __name__ == '__main__':
    t = int(input())
    res = []
    while t > 0:
        t -= 1
        ten = input()
        soCu = int(input())
        soMoi = int(input())
        hd = HoaDon(ten, soCu, soMoi)
        res.append(hd)
    res.sort(key = cmp_to_key(cmp))
    for x in res:
        print(x)