from math import *

def check(s):
    if len(s) % 2 == 0:
        return False
    tmp = s[0]
    if s[0] == s[1]:
        return False
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != tmp:
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
        