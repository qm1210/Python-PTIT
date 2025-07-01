from math import *

if __name__ == '__main__':
    s = input()
    n = int(s)
    tmp = ""
    res = ""
    while n > 0:
        l = n % 1000
        sum = 0
        if len(str(l)) == 1:
            tmp = "00" + str(l)
        elif len(str(l)) == 2:
            tmp = "0" + str(l)
        else:
            tmp = str(l)
        n = n // 1000
        rev = tmp[::-1]
        for i in range(len(rev)):
            if rev[i] == "1":
                sum += 2 ** i
        res += str(sum)
    res = res[::-1]
    print(res)
            
