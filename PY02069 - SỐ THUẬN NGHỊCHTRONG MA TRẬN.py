from math import *
import sys

class DoiXung:
    def __init__(self, i, j, giaTri):
        self.i = i
        self.j = j
        self.giaTri = giaTri
    
    def geti(self):
        return self.i
    
    def getj(self):
        return self.j
    
    def getGiaTri(self):
        return self.giaTri

def doiXung(n):
    if n < 10:
        return False
    s = str(n)
    if s != s[::-1]:
        return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    check = False
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    res = []
    max_val = -99
    for i in range(n):
        for j in range(m):
            if doiXung(a[i][j]):
                check = True
                dx = DoiXung(i, j, a[i][j])
                res.append(dx)
                if a[i][j] > max_val:
                    max_val = a[i][j]
    if check:
        print(max_val)
        for x in res:
            if x.getGiaTri() == max_val:
                print(f"Vi tri [{x.geti()}][{x.getj()}]")
    else:
        print("NOT FOUND")