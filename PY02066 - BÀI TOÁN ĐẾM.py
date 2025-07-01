from math import *
import sys

if __name__ == '__main__':
    n = int(input())
    data = ""
    check = False
    for line in sys.stdin:
        data += line.strip() + " "
    a = list(map(int, data.split()))
    max_val = max(a)
    for i in range(1, max_val + 1):
        if i not in a:
            check = True
            print(i)
    if not check:
        print("Excellent!")
    