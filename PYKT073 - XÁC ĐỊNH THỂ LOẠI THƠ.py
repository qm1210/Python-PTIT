from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    t = int(input())
    arr = []
    while t > 0:
        t -= 1
        s = input()
        arr.append(s)
    res = []
    current = []
    for line in arr:
        current.append(line)
        if len(current) >= 2 and len(current) % 2 == 0:
            if len(current) == 4:
                check = True
                for x in current:
                    a = x.split()
                    if len(a) != 7:
                        check = False
                        break
                if check:
                    res.append("2")
                current = []
            elif len(current) >= 2 and len(current) % 2 == 0:
                check = True
                for i in range(0, len(current), 2):
                    a = current[i].split()
                    b = current[i + 1].split()
                    if len(a) != 6 or len(b) != 8:
                        check = False
                        break
                if check:
                    if not res or res[-1] != "1":
                        res.append("1")
                    current = []
    print(len(res))
    for x in res:
        print(x)