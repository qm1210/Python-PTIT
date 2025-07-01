from decimal import Decimal
from functools import cmp_to_key
from math import *

class ThiSinh:
    def __init__(self, ten, ngaysinh, d1, d2, d3):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.tongdiem = d1 + d2 + d3
    
    def __str__(self):
        return self.ten + " " + self.ngaysinh + " " + format("%.1f" % self.tongdiem)

if __name__ == '__main__':
    ten = input()
    ngaysinh = input()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    ts = ThiSinh(ten, ngaysinh, d1, d2, d3)
    print(ts)