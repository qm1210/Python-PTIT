from math import *

def tamPhan(n):
    tmp = "012"
    res = ""
    while n > 0:
        res += tmp[n % 3]
        n //= 3
    return res[::-1]

def check(s):
    cnt2 = 0
    for i in range(len(s)):
        if s[i] == '2':
            cnt2 += 1
    if cnt2 > len(s) / 2:
        return True
    return False

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        cnt = 0
        i = 1
        n = int(input())
        while cnt < n:
            x = tamPhan(i)
            if check(x):
                print(x, end=" ")
                cnt += 1
            i += 1
        print()
            
