from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class SinhVien:
    cnt = 1
    def __init__(self, ten, d1, d2, d3):
        self.ten = self.chuanHoa(ten)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.ma = f"SV{SinhVien.cnt:02d}"
        SinhVien.cnt += 1
        self.diem = ceil((d1 * 3 + d2 * 3 + d3 * 2) / 8 * 100) / 100

    def chuanHoa(self, ten):
        tmp = ""
        a = ten.split()
        for x in a:
            tmp += x.capitalize() + " "
        return tmp.strip()
        
    def __str__(self):
        return f"{self.ma} {self.ten} {self.diem:.2f}"

def cmp(a, b):
    if a.diem < b.diem:
        return 1
    elif a.diem > b.diem:
        return -1
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
        d1 = float(input())
        d2 = float(input())
        d3 = float(input())
        sv = SinhVien(ten, d1, d2, d3)
        arr.append(sv)
    arr.sort(key=cmp_to_key(cmp))
    cnt = 1
    print(f"{arr[0]} {cnt}")
    for i in range(1, len(arr)):
        if arr[i].diem != arr[i - 1].diem:
            cnt = i + 1
        print(f"{arr[i]} {cnt}")