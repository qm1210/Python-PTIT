from decimal import Decimal
from functools import cmp_to_key
from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        
    def toiGian(self):
        ucln = gcd(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln
    
    def __str__(self):
        return str(int(self.tu)) + '/' + str(int(self.mau))

if __name__ == '__main__':
    tu, mau = map(int, input().split())
    p = PhanSo(tu, mau)
    p.toiGian()
    print(p)
