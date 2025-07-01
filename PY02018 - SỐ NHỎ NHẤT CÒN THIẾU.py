from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    smallest = 1
    for i in a:
        if smallest == i:
            smallest += 1
    print(smallest)
