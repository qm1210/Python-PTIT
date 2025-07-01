from math import *

def check(s):
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
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

