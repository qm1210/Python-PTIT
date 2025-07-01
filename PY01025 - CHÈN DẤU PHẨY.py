from math import *

if __name__ == '__main__':
    s = input()
    res = []
    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        res.append(s[i])
        cnt += 1
        if cnt == 3 and i != 0:
            cnt = 0
            res.append(",")
    res.reverse()
    print("".join(map(str, res)))
    