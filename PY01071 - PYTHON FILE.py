from math import *

if __name__ == '__main__':
    s = input().strip().lower()
    a = s.split(".")
    if a[1] == "py":
        print("yes")
    else:
        print("no")