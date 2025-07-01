from decimal import Decimal
from functools import cmp_to_key
from math import *


if __name__ == '__main__':
    tu1, mau1, tu2, mau2 = map(int, input().split())
    bcnn = (mau1 * mau2) // gcd(mau1, mau2)
    tu1 *= bcnn // mau1
    tu2 *= bcnn // mau2
    tu = tu1 + tu2
    mau = bcnn
    ucln = gcd(tu, mau)
    tu //= ucln
    mau //= ucln
    print(f"{tu}/{mau}")
