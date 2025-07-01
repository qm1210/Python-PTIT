from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class KhachHang:
    cnt = 1
    def __init__(self, ten, soPhong, ngayNhan, ngayTra, tiendv):
        self.ma = "KH" + f"{KhachHang.cnt:02d}"
        KhachHang.cnt += 1
        self.ten = ten
        self.soPhong = soPhong
        self.ngayNhan = ngayNhan
        self.ngayTra = ngayTra
        self.tiendv = tiendv
        self.dateNhan = datetime.strptime(ngayNhan, "%d/%m/%Y")
        self.dateTra = datetime.strptime(ngayTra, "%d/%m/%Y")
        self.ngay = (self.dateTra - self.dateNhan).days + 1
        if self.soPhong[0] == "1":
            self.tien = 25 * self.ngay + self.tiendv
        elif self.soPhong[0] == "2":
            self.tien = 34 * self.ngay + self.tiendv
        elif self.soPhong[0] == "3":
            self.tien = 50 * self.ngay + self.tiendv
        else:
            self.tien = 80 * self.ngay + self.tiendv
        
    def __str__(self):
        return f"{self.ma} {self.ten} {self.soPhong} {self.ngay} {self.tien}"

def cmp(a, b):
    if a.tien < b.tien:
        return 1
    elif a.tien > b.tien:
        return -1

if __name__ == '__main__':
    t = int(input())
    arr = []
    while t > 0:
        t -= 1
        kh = KhachHang(input().strip(), input().strip(), input().strip(), input().strip(), int(input()))
        arr.append(kh)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)