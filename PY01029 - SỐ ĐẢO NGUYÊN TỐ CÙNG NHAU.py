from math import *

def check(s1, s2):
    n1 = int(s1)
    n2 = int(s2)
    if gcd(n1, n2) != 1:
        return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s1 = input()
        s2 = s1[::-1]
        if check(s1, s2):
            print("YES")
        else:
            print("NO")

    