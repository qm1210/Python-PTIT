from math import *
from collections import *
import re

class Xe:
    def __init__(self, bienSo, loaiXe, soGhe, huongDi, ngay):
        self.bienSo = bienSo
        self.loaiXe = loaiXe
        self.soGhe = int(soGhe)
        self.huongDi = huongDi
        self.ngay = ngay
        if self.huongDi == "IN":
            if self.loaiXe == "Xe_con":
                if self.soGhe == 5:
                    self.tien = 10000
                elif self.soGhe == 7:
                    self.tien = 15000
            elif self.loaiXe == "Xe_tai":
                self.tien = 20000
            else:
                if self.soGhe == 29:
                    self.tien = 50000
                else:
                    self.tien = 70000
        else:
            self.tien = 0

if __name__ == '__main__':
    t = int(input())
    mp = {}
    arr = []
    while t > 0:
        t -= 1
        bienSo, loaiXe, soGhe, huongDi, ngay = map(str, input().split())
        xe = Xe(bienSo, loaiXe, soGhe, huongDi, ngay)
        arr.append(xe)
        if ngay not in mp:
            mp[ngay] = 1
    for x in mp:
        total = 0
        for xe in arr:
            if xe.ngay == x:
                total += xe.tien
        print(x, total, sep=": ")


