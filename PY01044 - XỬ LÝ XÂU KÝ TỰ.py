from math import *

if __name__ == '__main__':
    s1 = input().lower()
    s2 = input().lower()
    a = s1.split()
    b = s2.split()
    se1 = set(a)
    se2 = set(b)
    hop = se1.union(se2)
    giao = se1.intersection(se2)
    hop = sorted(list(hop))
    giao = sorted(list(giao))
    print(" ".join(hop))
    print(" ".join(giao))