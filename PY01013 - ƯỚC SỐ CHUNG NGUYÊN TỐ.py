from math import *

def check(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        a, b = map(int, input().split())
        c = str(gcd(a, b))
        sum = 0
        for i in range(len(c)):
            sum += int(c[i])
        if check(sum):
            print("YES")
        else:
            print("NO")