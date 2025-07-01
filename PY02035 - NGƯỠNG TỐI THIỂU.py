from math import *

if __name__ == '__main__':
    s = input()
    k = int(input())
    mp = {}
    check = False
    for i in range(0, len(s), 2):
        tmp = s[i:i + 2]
        n = int(tmp)
        if n not in mp:
            mp[n] = 1
        else:
            mp[n] += 1
    a = sorted(list(mp.keys())) 
    for x in a:
        if mp[x] >= k:
            check = True
            print(x, mp[x], sep=' ')
    if not check:
        print("NOT FOUND")