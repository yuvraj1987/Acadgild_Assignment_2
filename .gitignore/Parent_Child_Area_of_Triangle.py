# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:05:36 2018

@author: jkdadhich
"""

class Parent_Triangle(): # Parent Class Created
    def triangle_sides(self, side_A,side_B, side_C):
        # Initialize parameter
        self.side_A = side_A
        self.side_B = side_B
        self.side_C = side_C
        self.area   = 0


class Child_Triangle(Parent_Triangle): # Created Child Class or SubClass
    def calculateArea(self): # Calulating area
        s = (self.side_A + self.side_B + self.side_C)/2
        self.area = (s*(s-self.side_A)*(s-self.side_B)*(s-self.side_C))**0.5
        Child_Triangle.display_Result(self)
        return round(self.area,2)

    def display_Result(self): # printing result over screen
        print ("~~*~~"*10)
        print (" 1st Side of Triangle is :\t",self.side_A)
        print (" 2nd Side of Triangle is :\t",self.side_B)
        print (" 3rd Side of Triangle is :\t",self.side_C)
        print ("~~*~~"*10)
        print (" Area of Triangle is :\t",round(self.area,2))
        print ("~~*~~"*10)

Object_Child = Child_Triangle()
Object_Child.triangle_sides(4,2,5)
Object_Child.calculateArea()

