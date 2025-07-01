from math import *

def check(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 10 != 0:
        return False
    for i in range(len(n) - 1):
        m = int(n[i]) - int(n[i + 1])
        if abs(m) != 2:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")