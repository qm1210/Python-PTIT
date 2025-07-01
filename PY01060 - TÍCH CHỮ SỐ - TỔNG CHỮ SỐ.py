from math import *

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        sum = 0
        tich = 1
        check = 0
        for i in range(len(s)):
            if i % 2 != 0:
                sum += int(s[i])
            if i % 2 == 0:
                if s[i] != '0':
                    check = 1
                    tich *= int(s[i])
        if check == 0:
            tich = 0
        print(f"{tich} {sum}")
        