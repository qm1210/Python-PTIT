from math import isqrt

def check(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    nt = []
    a = list(map(int, input().split()))
    for i in range(n):
        if check(a[i]):
            nt.append(a[i])
    nt.sort()
    for i in range(n):
        if check(a[i]):
            a[i] = nt.pop(0)
    print(*a)