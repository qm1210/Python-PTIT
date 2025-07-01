from math import isqrt

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    se1 = set(a)
    se2 = set(b)
    if se1 == se2:
        print("YES")
    else:
        print("NO")