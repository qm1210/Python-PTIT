from math import *

if __name__ == '__main__':
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '4' or s[i] == '7':
            cnt += 1
    if cnt == 7 or cnt == 4:
        print("YES")
    else:
        print("NO")

