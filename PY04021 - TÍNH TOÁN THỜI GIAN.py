from decimal import Decimal
from functools import cmp_to_key
from math import *

def cmp(a, b):
    if a.thoigian < b.thoigian:
        return 1
    else:
        return -1

def chuanHoa(ten):
    a = ten.split()
    res = []
    for x in a:
        res.append(x.capitalize())
    return ' '.join(res)

def minutes(gioVao, gioRa):
    hv, mv = gioVao.split(':')
    hr, mr = gioRa.split(':')
    return (int(hr) - int(hv)) * 60 + int(mr) - int(mv)

class Gamer:
    def __init__(self, id, ten, gioVao, gioRa):
        self.id = id
        self.ten = chuanHoa(ten)
        self.gioVao = gioVao
        self.gioRa = gioRa
        self.avg = 0
        self.thoigian = minutes(gioVao, gioRa)
    
    def __str__(self):
        return self.id + " " + self.ten + " " + str(self.thoigian // 60) + " gio " + str(self.thoigian % 60) + " phut"
        
if __name__ == '__main__':
    t = int(input())
    res = []
    while t > 0:
        t -= 1
        id = input().strip()
        ten = input().strip()
        gioVao = input().strip()
        gioRa = input().strip()
        g = Gamer(id, ten, gioVao, gioRa)
        res.append(g)
    res.sort(key=lambda x: -x.thoigian)
    for x in res:
        print(x)