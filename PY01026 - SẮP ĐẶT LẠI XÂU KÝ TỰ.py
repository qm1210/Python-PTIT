from math import *
import sys

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s1 = input()
        s2 = input()
        tmp1 = []
        tmp2 = []
        check = False
        if len(s1) != len(s2):
            check = False
        else:
            for i in range(len(s1)):
                tmp1.append(s1[i])
                tmp2.append(s2[i])
            tmp1.sort()
            tmp2.sort()
            if tmp1 == tmp2:
                check = True
        if check:
            print(f"Test {_ + 1}: YES")
        else:
            print(f"Test {_ + 1}: NO")
