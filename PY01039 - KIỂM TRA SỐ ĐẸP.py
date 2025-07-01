from math import *

def check(s):
    unit = set(s)
    if len(unit) > 2:
        return False
    for i in range(0, len(s) - 2):
        if s[i] != s[i + 2]:
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
        
        
