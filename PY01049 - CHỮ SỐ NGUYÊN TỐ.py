from math import *

def check(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def checkyc(s):
    if check(len(s)) == False:
        return False
    cntnt = 0
    cntk = 0
    for i in range(0, len(s)):
        if check(int(s[i])):
            cntnt += 1
        else:
            cntk += 1
    if cntnt <= cntk:
        return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        if checkyc(s):
            print("YES")
        else:
            print("NO")