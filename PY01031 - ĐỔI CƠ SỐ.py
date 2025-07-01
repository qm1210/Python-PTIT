from math import *

if __name__ == '__main__':
    t = int(input())
    tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while t > 0:
        t -= 1
        res = ""
        n, b = map(int, input().split())
        while n > 0:
            x = n % b
            res += tmp[x]
            n //= b
        res = res[::-1]
        print(res)