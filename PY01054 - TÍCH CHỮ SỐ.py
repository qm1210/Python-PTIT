from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        tich = 1
        for i in range(len(s)):
            if s[i] != '0':
                tich *= int(s[i])
        print(tich)
        