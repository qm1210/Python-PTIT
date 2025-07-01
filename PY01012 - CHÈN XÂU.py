from math import *

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    p = int(input())
    p -= 1
    s = s1[:p] + s2 + s1[p:]
    print(s)
