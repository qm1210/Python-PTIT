from math import *

if __name__ == '__main__':
    s = input()
    mp = {}
    for i in range(0, len(s), 2):
        tmp = s[i:i + 2]
        n = int(tmp)
        if n >= 10 and n <= 99 and n not in mp:
            mp[n] = 1
    a = list(mp.keys())
    print(*a)