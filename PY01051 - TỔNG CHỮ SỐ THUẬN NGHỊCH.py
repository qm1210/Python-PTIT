from math import *

def check(s):
    if len(s) < 2:
        return False
    rev = s[::-1]
    if s != rev:
        return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        total = 0
        for i in range(len(s)):
            total += int(s[i])
        if check(str(total)):
            print("YES")
        else:
            print("NO")
        