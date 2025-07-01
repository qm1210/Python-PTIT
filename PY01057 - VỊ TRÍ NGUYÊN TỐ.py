from math import *

def checknt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    for i in range(len(s)):
        if checknt(i) and checknt(int(s[i])) == False:
            return False
        if checknt(i) == False and checknt(int(s[i])):
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
        