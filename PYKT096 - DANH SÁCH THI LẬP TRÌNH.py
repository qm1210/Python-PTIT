from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

class Team:
    cnt = 1
    def __init__(self, tenTeam, truong):
        self.tenTeam = tenTeam
        self.truong = truong
        self.ma = f"Team{Team.cnt:02d}"
        Team.cnt += 1

class ThiSinh:
    cnt = 1
    def __init__(self, ten, Team):
        self.ten = ten
        self.Team = Team
        self.maTS = f"C{ThiSinh.cnt:03d}"
        ThiSinh.cnt += 1

    def __str__(self):
        return f"{self.maTS} {self.ten} {self.Team.tenTeam} {self.Team.truong}"

def cmp(a, b):
    if a.ten < b.ten:
        return -1
    else:
        return 1        

if __name__ == '__main__':
    t = int(input())
    arrt = []
    arr = []
    while t > 0:
        t -= 1
        tenTeam = input()
        truong = input()
        te = Team(tenTeam, truong)
        arrt.append(te)
    t = int(input())
    while t > 0:
        t -= 1
        ten = input()
        ma = input()
        for te in arrt:
            if te.ma == ma:
                ts = ThiSinh(ten, te)
                arr.append(ts)
                break
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)