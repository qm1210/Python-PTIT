from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        n = input()
        l = len(n)
        cnt = 0
        i = 0
        while i < len(s):
            tmp = s[i:i+l]
            if tmp == n:
                cnt += 1
                i += l
            else:
                i += 1
        print(cnt)               