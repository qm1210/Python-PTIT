from math import *

if __name__ == '__main__':
    n = int(input())
    res = []
    while n > 0:
        tmp = n % 1000
        n //= 1000
        total = 0
        s = f"{tmp:03d}"
        rev = s[::-1]
        for i in range(len(rev)):
            total += 2 ** i * int(rev[i])
        res.append(str(total))
    reversed(res)
    print("".join(map(str, reversed(res))))