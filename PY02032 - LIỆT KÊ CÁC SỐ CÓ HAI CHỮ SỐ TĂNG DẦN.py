from math import isqrt

if __name__ == '__main__':
    s = input()
    se = set()
    for i in range(0, len(s), 2):
        tmp = s[i:i + 2]
        n = int(tmp)
        if n >= 10 and n <= 99:
            se.add(n)
    a = sorted(list(se))
    print(*a)