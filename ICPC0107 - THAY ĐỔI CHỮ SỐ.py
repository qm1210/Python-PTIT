if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        p, q = input().split()
        x1 = input().strip()
        if len(x1.split()) > 1:
            x1, x2 = x1.split()
        else:
            x2 = input().strip()
        small = min(p, q)
        large = max(p, q)
        min_x1 = x1.replace(p, small).replace(q, small)
        min_x2 = x2.replace(p, small).replace(q, small)
        max_x1 = x1.replace(p, large).replace(q, large)
        max_x2 = x2.replace(p, large).replace(q, large)
        min_val = int(min_x1) + int(min_x2)
        max_val = int(max_x1) + int(max_x2)
        print(min_val, max_val)