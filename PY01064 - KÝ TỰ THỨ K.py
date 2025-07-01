from math import *

if __name__ == '__main__':
    tmp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        s = "A"
        cnt = 1
        while cnt < n:
            s = s + tmp[cnt] + s
            cnt += 1
        print(s[k - 1])
