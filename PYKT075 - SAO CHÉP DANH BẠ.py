from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class DienThoai:
    def __init__(self, ngay, ten, sdt):
        self.ngay = ngay
        self.ten = self.chuanHoa(ten)
        self.sdt = sdt
    
    def chuanHoa(self, ten):
        tmp = ""
        a = ten.split()
        for i in range(len(a)):
            tmp += a[i].capitalize() + " "
        return tmp.strip()
    
    def __str__(self):
        return f"{self.ten}: {self.sdt} {self.ngay}"

def cmp(a, b):
    a1 = a.ten.split()
    a2 = b.ten.split()
    ho1 = a1[:-1]
    ho2 = a2[:-1]
    if a1[-1] < a2[-1]:
        return -1
    elif a1[-1] > a2[-1]:
        return 1
    else:
        if ho1 < ho2:
            return -1
        else:
            return 1

if __name__ == '__main__':
    f = open('SOTAY.txt', 'r')
    vb = [lines.strip() for lines in f.readlines()]
    i = 0
    res = []
    current = ""
    while i < len(vb):
        if vb[i].strip().startswith("Ngay"):
            a = vb[i].strip().split()
            current = a[1]
        else:
            ten = vb[i].strip()
            sdt = vb[i + 1].strip()
            i += 1
            res.append(DienThoai(current, ten, sdt))
        i += 1
    res.sort(key=cmp_to_key(cmp))
    for x in res:
        print(x)