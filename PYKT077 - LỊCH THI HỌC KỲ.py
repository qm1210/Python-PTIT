from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class MonHoc:
    def __init__(self, maMon, tenMon):
        self.maMon = maMon
        self.tenMon = tenMon

class LichThi:
    cnt = 1
    def __init__(self, MonHoc, ngay, gio, nhom):
        self.MonHoc = MonHoc
        self.ngay = ngay
        self.gio = gio
        self.nhom = nhom
        self.ma = "T" + f"{LichThi.cnt:03d}"
        LichThi.cnt += 1

    def __str__(self):
        return f"{self.ma} {self.MonHoc.maMon} {self.MonHoc.tenMon} {self.ngay} {self.gio} {self.nhom}"

def cmp(a, b):
    date1 = datetime.strptime(a.ngay, "%d/%m/%Y")
    date2 = datetime.strptime(b.ngay, "%d/%m/%Y")
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        if a.gio < b.gio:
            return -1
        elif a.gio > b.gio:
            return 1
        else:
            if a.MonHoc.maMon < b.MonHoc.maMon:
                return -1
            else:
                return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    arrmh = []
    arr = []
    while n > 0:
        n -= 1
        maMon = input().strip()
        tenMon = input().strip()
        mh = MonHoc(maMon, tenMon)
        arrmh.append(mh)
    while m > 0:
        m -= 1
        maMon, ngay, gio, nhom = input().split()
        for mh in arrmh:
            if mh.maMon == maMon:
                lt = LichThi(mh, ngay, gio, nhom)
                arr.append(lt)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)