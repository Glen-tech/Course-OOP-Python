# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:55:56 2021

@author: glen_
"""

class Rectangle:
    
    def __init__(self, length, width):
        print(self)
        self.length = length
        self.width = width
        
        
my_rectangle = Rectangle(5,10)

print(my_rectangle.length)
print(my_rectangle.width)

my_rectangle2 = Rectangle(length = 10, width = 20)
print(my_rectangle2.length)
print(my_rectangle2.width)


