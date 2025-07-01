from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *
from heapq import *

def sinh(s):
    res = []
    for i in range(10, 100):
        ok = True
        tmp = str(i)
        for j in range(len(s)):
            if s[j] != "?" and s[j] != tmp[j]:
                ok = False
                break
        if ok:
            res.append(i)
    return res

def check(s, tmp):
    for i in range(len(s)):
        if s[i] != "?" and s[i] != tmp[i]:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        bt = s.split()
        a, op, b, c = bt[0], bt[1], bt[2], bt[4]
        lista = sinh(a)
        listb = sinh(b)
        res = []
        if op == "?":
            listop = ["+", "-", "*", "/"]
        else:
            listop = [op]
        for A in lista:
            for B in listb:
                for OP in listop:
                    if OP == "+":
                        C = A + B
                    elif OP == "-":
                        C = A - B
                    elif OP == "*":
                        C = A * B
                    else:
                        if B == 0 or A % B != 0:
                            continue
                        C = A // B
                    if C < 10 or C > 99:
                        continue
                    tmp = f"{A} {OP} {B} = {C}"
                    if check(s, tmp):
                        res.append(tmp)
        if res:
            print(res[0])
        else:
            print("WRONG PROBLEM!")