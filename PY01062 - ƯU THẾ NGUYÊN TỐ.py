from math import *

def checknt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    if checknt(len(s)) == False:
        return False
    cnt0 = 0
    cntnt = 0
    for i in range(len(s)):
        if checknt(int(s[i])):
            cntnt += 1
        else:
            cnt0 += 1
    if cntnt <= cnt0:
        return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")