from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key

class SinhVien:
    def __init__(self, msv, ten, lop):
        self.msv =  msv
        self.ten = ten
        self.lop = lop
    
    def __str__(self):
        return f"{self.msv} {self.ten} {self.lop}"

if __name__ == '__main__':
    t = int(input())
    q = t
    arr = []
    mp = {}
    while t > 0:
        t -= 1
        msv = input()
        ten = input()
        lop = input()
        sv = SinhVien(msv, ten, lop)
        arr.append(sv)
    while q > 0:
        q -= 1
        msv, s = map(str, input().split())
        diem = 10
        dk = ""
        for x in arr:
            if msv == x.msv:
                for c in s:
                    if c == "m":
                        diem -= 1
                    elif c == "v":
                        diem -= 2
                if diem < 0:
                    diem = 0
                if x not in mp:
                    mp[x] = diem
                break
    for x in arr:
        if mp[x] == 0:
            print(x, mp[x], "KDDK", sep=" ")
        else:
            print(x, mp[x], sep=" ")