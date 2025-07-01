from math import isqrt

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        mp = {}
        for i in range(n):
            if a[i] in mp:
                mp[a[i]] += 1
            else:
                mp[a[i]] = 1
        for x in mp:
            if mp[x] % 2 == 1:
                print(x)
                break