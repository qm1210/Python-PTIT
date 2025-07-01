from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        res = []
        lst = []
        for i in range(len(s)):
            lst.append(s[i])
            if i == len(s) - 1 or s[i] != s[i + 1]:
                cnt = len(lst)
                lst.clear()
                res.append(cnt)
                res.append(s[i])
        print("".join(map(str, res)))