from math import *

if __name__ == '__main__':
    s = input()
    i = 0
    check = True
    while i < len(s):
        if s[i:i + 3] == "688":
            i += 3
        elif s[i:i + 2] == "68":
            i += 2
        elif s[i:i + 1] == "6":
            i += 1
        else:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")