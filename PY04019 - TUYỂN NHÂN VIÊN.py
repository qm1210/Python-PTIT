from decimal import Decimal
from functools import cmp_to_key
from math import *

def cmp(a, b):
    if a.avg < b.avg:
        return 1
    else:
        return -1

class NhanVien:
    cnt = 1
    def __init__(self, ten, diemlt, diemth):
        self.id = f"TS0{NhanVien.cnt}"
        NhanVien.cnt += 1
        self.ten = ten
        self.diemlt = diemlt
        self.diemth = diemth
        self.avg = (diemlt + diemth) / 2
        if self.avg < 5:
            self.danhgia = "TRUOT"
        elif self.avg < 8:
            self.danhgia = "CAN NHAC"
        elif self.avg <= 9.5:
            self.danhgia = "DAT"
        else:
            self.danhgia = "XUAT SAC"
    
    def __str__(self):
        return self.id + " " + self.ten + " " + f"{self.avg:.2f}" + " " + self.danhgia

if __name__ == '__main__':
    t = int(input())
    res = []
    while t > 0:
        t -= 1
        ten = input()
        diemlt = float(input())
        diemth = float(input())
        if diemlt > 10:
            diemlt /= 10
        if diemth > 10:
            diemth /= 10
        nv = NhanVien(ten, diemlt, diemth)
        res.append(nv)
    res.sort(key = cmp_to_key(cmp))
    for x in res:
        print(x)
