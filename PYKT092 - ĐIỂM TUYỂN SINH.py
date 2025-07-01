from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class ThiSinh:
    cnt = 1
    def __init__(self, ten, diem, dt, kv):
        self.ten = self.chuanHoa(ten)
        self.diem = diem
        self.dt = dt
        self.kv = kv
        self.ma = f"TS{ThiSinh.cnt:02d}"
        ThiSinh.cnt += 1
        self.ut = 0
        if self.kv == "1":
            self.ut = 1.5
        elif self.kv == "2":
            self.ut = 1
        else:
            self.ut = 0
        if self.dt != "Kinh":
            self.ut += 1.5
        self.final = self.diem + self.ut
        if self.final >= 20.5:
            self.tt = "Do"
        else:
            self.tt = "Truot"

    def chuanHoa(self, ten):
        a = ten.split()
        tmp = ""
        for x in a:
            tmp += x.capitalize() + " "
        return tmp.strip()
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.final:.1f} {self.tt}"

def cmp(a, b):
    if a.final > b.final:
        return -1
    elif a.final < b.final:
        return 1
    else:
        if a.ma < b.ma:
            return -1
        else:
            return 1

if __name__ == '__main__':
    t = int(input())
    arr = []
    while t > 0:
        t -= 1
        ten = input().strip()
        diem = float(input())
        dt = input().strip()
        kv = input().strip()
        ts = ThiSinh(ten, diem, dt, kv)
        arr.append(ts)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)
