from math import *

def check(n):
    if n % 3 != 0:
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
        if check(total):
            print("YES")
        else:
            print("NO")
        