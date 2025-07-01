from functools import cmp_to_key
from math import *
from collections import *
from datetime import *

class Tram:
    def __init__(self, ten, start, end, mua):
        self.ten = ten
        self.start = start
        self.end = end
        self.mua = mua
        self.timestart = datetime.strptime(start, "%H:%M")
        self.timeend = datetime.strptime(end, "%H:%M")
        self.time = ((self.timeend - self.timestart).seconds) / 3600

if __name__ == '__main__':
    t = int(input())
    ma = {}
    lm = {}
    cnt = 1
    tg = {}
    while t > 0:
        t -= 1
        ten = input().strip()
        start = input().strip()
        end = input().strip()
        mua = int(input())
        tr = Tram(ten, start, end, mua)
        if ten not in ma:
            ma[ten] = f"T{cnt:02d}"
            cnt += 1
        if ten not in lm:
            lm[ten] = mua
        else:
            lm[ten] += mua
        if ten not in tg:
            tg[ten] = tr.time
        else:
            tg[ten] += tr.time
    for x in ma:
        avg = lm[x] / tg[x]
        print(f"{ma[x]} {x} {avg:.2f}")