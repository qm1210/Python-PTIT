from math import *

s = str(input())
cntlower = 0
cntupper = 0
for i in range(0, len(s)):
    if s[i].islower():
        cntlower += 1
    else:
        cntupper += 1
if cntupper > cntlower:
    s = s.upper()
else:
    s = s.lower()
print(s)