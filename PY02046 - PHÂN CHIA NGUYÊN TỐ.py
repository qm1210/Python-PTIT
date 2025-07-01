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
    a = list(map(int, input().split()))
    mp = {}
    for i in range(n):
        if a[i] not in mp:
            mp[a[i]] = 1
    b = []
    b = list(mp.keys())
    total = sum(b)
    for i in range(len(b)):
        if check(sum(b[:i+1:])) and check(sum(b[i+1:])):
            print(i)
            break
    else:
        print("NOT FOUND")
