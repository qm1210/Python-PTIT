from math import *

def check(n):
    for i in range(0, len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = list(input())
        if check(n):
            print("YES")
        else:
            print("NO")