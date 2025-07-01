from math import *

def check(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    se = set()
    for i in range(len(a)):
        if check(a[i]) and a[i] not in se:
            se.add(a[i])
            print(f"{a[i]} {a.count(a[i])}")