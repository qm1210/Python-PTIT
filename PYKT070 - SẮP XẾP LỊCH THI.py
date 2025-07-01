from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class MonThi:
    def __init__(self, maMon, ten, hinhThuc):
        self.maMon = maMon
        self.ten = ten
        self.hinhThuc = hinhThuc

class CaThi:
    cnt = 1
    def __init__(self, ngay, gio, phong):
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.maCa = "C" + f"{CaThi.cnt:03d}"
        CaThi.cnt += 1

class LichThi:
    def __init__(self, CaThi, MonThi, maNhom, soSV):
        self.CaThi = CaThi
        self.MonThi = MonThi
        self.maNhom = maNhom
        self.soSV = soSV

    def __str__(self):
        return f"{self.CaThi.ngay} {self.CaThi.gio} {self.CaThi.phong} {self.MonThi.ten} {self.maNhom} {self.soSV}"

def cmp(a, b):
    if a.CaThi.ngay < b.CaThi.ngay:
        return -1
    elif a.CaThi.ngay > b.CaThi.ngay:
        return 1
    else:
        if a.CaThi.gio < b.CaThi.gio:
            return -1
        elif a.CaThi.gio > b.CaThi.gio:
            return 1
        else:
            if a.CaThi.maCa < b.CaThi.maCa:
                return -1
            else:
                return 1

if __name__ == '__main__':
    f = open('MONTHI.in', 'r')
    t = int(f.readline())
    arrmt = []
    arrct = []
    arrlt = []
    while t > 0:
        t -= 1
        maMon = f.readline().strip()
        ten = f.readline().strip()
        hinhThuc = f.readline().strip()
        mt = MonThi(maMon, ten, hinhThuc)
        arrmt.append(mt)
    f = open('CATHI.in', 'r')
    t = int(f.readline())
    while t > 0:
        t -= 1
        ngay = f.readline().strip()
        gio = f.readline().strip()
        phong = f.readline().strip()
        ct = CaThi(ngay, gio, phong)
        arrct.append(ct)
    f = open('LICHTHI.in', 'r')
    t = int(f.readline())
    while t > 0:
        t -= 1
        maCa, maMon, maNhom, soSV = f.readline().strip().split()
        for ct in arrct:
            if ct.maCa == maCa:
                for mt in arrmt:
                    if mt.maMon == maMon:
                        lt = LichThi(ct, mt, maNhom, soSV)
                        arrlt.append(lt)
    arrlt.sort(key=cmp_to_key(cmp))
    for x in arrlt:
        print(x)

        

