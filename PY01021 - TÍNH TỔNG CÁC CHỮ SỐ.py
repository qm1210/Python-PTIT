from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        res = []
        cnt = 0
        for x in s:
            if x.isdigit():
                cnt += int(x)
            else:
                res.append(x)
        res.sort()
        res.append(str(cnt))
        print("".join(res))
