from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

dut = {"1":2.0, "2":1.5, "3":1.0, "4":0.0}
mon = {"A":"TOAN", "B":"LY", "C":"HOA"}

class MatHang:
    def __init__(self, ma, ten, soLuong, donGia, chietKhau):
        self.ma = ma
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.chietKhau = chietKhau
        self.tien = self.donGia * self.soLuong - self.chietKhau
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.soLuong} {self.donGia} {self.chietKhau} {self.tien}"

def cmp(a, b):
    if a.tien > b.tien:
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
        soLuong = int(input())
        donGia = int(input())
        chietKhau = int(input())
        mh = MatHang(ma, ten, soLuong, donGia, chietKhau)
        arr.append(mh)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)