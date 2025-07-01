from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class Phong:
    def __init__(self, maPhong, tenPhong):
        self.maPhong = maPhong
        self.tenPhong = tenPhong    
        
class NhanVien:
    def __init__(self, maNV, tenNV, luong, ngay, Phong):
        self.maNV = maNV
        self.tenNV = tenNV
        self.luong = luong
        self.ngay = ngay
        self.Phong = Phong
        self.loai = self.maNV[0]
        self.nam = int(self.maNV[1:3])
        if self.loai == "A":
            if self.nam >= 1 and self.nam <= 3:
                self.tien = self.luong * self.ngay * 10
            elif self.nam >= 4 and self.nam <= 8:
                self.tien = self.luong * self.ngay * 12
            elif self.nam >= 9 and self.nam <= 16:
                self.tien = self.luong * self.ngay * 14
            else:
                self.tien = self.luong * self.ngay * 20
        elif self.loai == "B":
            if self.nam >= 1 and self.nam <= 3:
                self.tien = self.luong * self.ngay * 10
            elif self.nam >= 4 and self.nam <= 8:
                self.tien = self.luong * self.ngay * 11
            elif self.nam >= 9 and self.nam <= 16:
                self.tien = self.luong * self.ngay * 13
            else:
                self.tien = self.luong * self.ngay * 16
        elif self.loai == "C":
            if self.nam >= 1 and self.nam <= 3:
                self.tien = self.luong * self.ngay * 9
            elif self.nam >= 4 and self.nam <= 8:
                self.tien = self.luong * self.ngay * 10
            elif self.nam >= 9 and self.nam <= 16:
                self.tien = self.luong * self.ngay * 12
            else:
                self.tien = self.luong * self.ngay * 14
        else:
            if self.nam >= 1 and self.nam <= 3:
                self.tien = self.luong * self.ngay * 8
            elif self.nam >= 4 and self.nam <= 8:
                self.tien = self.luong * self.ngay * 9
            elif self.nam >= 9 and self.nam <= 16:
                self.tien = self.luong * self.ngay * 11
            else:
                self.tien = self.luong * self.ngay * 13
        self.tien *= 1000
        
    def __str__(self):
        return f"{self.maNV} {self.tenNV} {self.Phong.tenPhong} {self.tien}"

if __name__ == '__main__':
    t = int(input())
    listPhong = []
    arr = []
    while t > 0:
        t -= 1
        s = input().strip()
        a = s.split()
        maPhong = a[0]
        tenPhong = ""
        for i in range(1, len(a)):
            tenPhong += a[i] + " "
        tenPhong = tenPhong.strip()
        p = Phong(maPhong, tenPhong)
        listPhong.append(p)
    t = int(input())
    while t > 0:
        t -= 1
        maNV = input().strip()
        tenNV = input().strip()
        luong = int(input())
        ngay = int(input())
        for p in listPhong:
            if p.maPhong == maNV[-2:]:
                nv = NhanVien(maNV, tenNV, luong, ngay, p)
                arr.append(nv)
                break
    for x in arr:
        print(x)




