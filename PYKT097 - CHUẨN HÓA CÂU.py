from math import *
from sys import *
from itertools import *
import re
from functools import cmp_to_key
from datetime import *

if __name__ == '__main__':
    vb = ""
    while True:
        try:
            s = input()
            if s == "":
                continue
            vb += s + "\n"
        except EOFError:
            break
    vb = vb.strip()
    a = re.split(r'[.?!]|\n', vb)
    b = re.findall(r'[.?!]|\n', vb)
    tmp = ""
    mark = 0
    for i in range(len(a)):
        a[i] = a[i].strip().capitalize()
        c = a[i].split()
        for j in range(len(c)):
            tmp += c[j] + " "
        tmp = tmp.strip()
        while mark < len(b):
            if b[mark] == "\n":
                if not tmp.endswith((".", "?", "!")):
                    tmp += "."
                tmp += "\n"
                mark += 1                    
                break
            else:
                tmp += b[mark] + "\n"
                mark += 1
                break
        if not tmp.strip().endswith((".", "!", "?")):
            tmp = tmp.strip() + "."
    print(tmp)
