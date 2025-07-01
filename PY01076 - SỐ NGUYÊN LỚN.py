from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        a = int(input())
        b = int(input())
        ucln = gcd(a, b)
        print(ucln)