from math import *

if __name__ == '__main__':
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while True:
        line = input()
        if line == '0':
            break
        k, s = line.split()
        k = int(k)
        res = []
        for i in range(len(s)):
            index = p.find(s[i])
            new = (index + k) % 28
            res.append(p[new])
        res.reverse()
        print("".join(map(str, res)))