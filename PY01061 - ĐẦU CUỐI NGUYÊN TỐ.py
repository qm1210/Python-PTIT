from math import *

def check(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        first = int(s[:3])
        last = int(s) % 1000
        if check(first) and check(last):
            print("YES")
        else:
            print("NO")