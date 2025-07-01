from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

dut = {"1":2.0, "2":1.5, "3":1.0, "4":0.0}
mon = {"A":"TOAN", "B":"LY", "C":"HOA"}

class GiaoVien:
    cnt = 1
    def __init__(self, ten, maxt, dt, dcm):
        self.ten = ten
        self.maxt = maxt
        self.dt = dt
        self.dcm = dcm
        self.mh = mon[self.maxt[0]]
        self.ma = "GV" + f"{GiaoVien.cnt:02d}"
        GiaoVien.cnt += 1
        self.diemut = dut[self.maxt[1]]
        self.diem = self.dt * 2 + self.dcm + self.diemut
        if self.diem > 18:
            self.tt = "TRUNG TUYEN"
        else:
            self.tt = "LOAI"

    def __str__(self):
        return f"{self.ma} {self.ten} {self.mh} {self.diem:.1f} {self.tt}"

def cmp(a, b):
    if a.diem > b.diem:
        return -1
    else:
        return 1

if __name__ == '__main__':
    t = int(input())
    arr = []
    while t > 0:
        t -= 1
        ten = input().strip()
        maxt = input().strip()
        dt = float(input())
        dcm = float(input())
        gv = GiaoVien(ten, maxt, dt, dcm)
        arr.append(gv)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)

