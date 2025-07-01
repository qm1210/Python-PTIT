from decimal import Decimal
from functools import cmp_to_key
from math import *
import sys

class Rectangle:
    def __init__(self, height, width, c):
        self.height = height
        self.width = width
        self.c = c.capitalize()
    
    def perimeter(self):
        return 2 * self.height + 2 * self.width
    
    def area(self):
        return self.height * self.width

    def color(self):
        return self.c

arr = input().split() 
if int(arr[0]) > 0 and int(arr[1]) > 0: 
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
    print("{} {} {}".format(r.perimeter(), r.area(), r.color())) 
else: print("INVALID")
sys.exit()

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))

