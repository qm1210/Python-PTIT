from decimal import Decimal
from functools import cmp_to_key
from math import *

class SoPhuc:
    def __init__(self, real, image):
        self.real = real
        self.image = image
    
    def __add__(self, other):
        return SoPhuc(self.real + other.real, self.image + other.image)

    def __mul__(self, other):
        return SoPhuc(self.real * other.real - self.image * other.image, self.real * other.image + self.image * other.real)

    def __str__(self):
        if self.image > 0:
            return f"{self.real} + {self.image}i"
        else:
            return f"{self.real} - {-self.image}i"

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        a, b, c, d = map(int, input().split())
        A = SoPhuc(a, b)
        B = SoPhuc(c, d)
        AB = A + B
        C = AB * A
        D = AB * AB
        print(C, end = ", ")
        print(D)