from math import *
from collections import *

def check(s):
    a = s.split(".")
    if len(a) != 4:
        return False
    for i in a:
        if not i.isdigit():
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")