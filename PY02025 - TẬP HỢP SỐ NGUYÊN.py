from math import isqrt

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    se1 = set(a)
    se2 = set(b)
    res1, res2, res3 = [], [], []
    res1 = list(se1 & se2)
    res2 = list(se1 - se2)
    res3 = list(se2 - se1)
    res1.sort()
    res2.sort()
    res3.sort()
    print(*res1)
    print(*res2)
    print(*res3)