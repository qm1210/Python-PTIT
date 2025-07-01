from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class TheLoai:
    cnt = 1
    def __init__(self, tentl):
        self.matl = "TL" + f"{TheLoai.cnt:03d}"
        TheLoai.cnt += 1
        self.tentl = tentl

class Phim:
    cnt = 1
    def __init__(self, TheLoai, ngay, tenPhim, tap):
        self.TheLoai = TheLoai
        self.ngay = ngay
        self.tenPhim = tenPhim
        self.tap = tap
        self.ma = "P" + f"{Phim.cnt:03d}"
        Phim.cnt += 1

    def __str__(self):
        return f"{self.ma} {self.TheLoai.tentl} {self.ngay} {self.tenPhim} {self.tap}"

def cmp(a, b):
    date1 = datetime.strptime(a.ngay, "%d/%m/%Y")
    date2 = datetime.strptime(b.ngay, "%d/%m/%Y")
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        if a.tenPhim < b.tenPhim:
            return -1 
        elif a.tenPhim > b.tenPhim:
            return 1
        else:
            if a.tap < b.tap:
                return -1
            else:
                return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    arrtl = []
    arr = []
    while n > 0:
        n -= 1
        tentl = input().strip()
        tl = TheLoai(tentl)
        arrtl.append(tl)
    while m > 0:
        m -= 1
        matl = input().strip()
        ngay = input().strip()
        tenPhim = input().strip()
        tap = input().strip()
        for tl in arrtl:
            if tl.matl == matl:
                p = Phim(tl, ngay, tenPhim, tap)
                arr.append(p)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)



        

