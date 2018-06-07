# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:05:36 2018

@author: jkdadhich
"""

class Triangle_Area():
    def __init__(self, side_A,side_B, side_C):
        # Initialize parameter
        self.side_A = side_A
        self.side_B = side_B
        self.side_C = side_C
        self.area   = 0

    def Area_caluation(self): # Function calulating perimeter and area
        Perimeter = (self.side_A+self.side_B+self.side_C)/2
        s = Perimeter
        self.area = (s*(s-self.side_A)*(s-self.side_B)*(s-self.side_C))**0.5
        Triangle_Area.Display_input(self)
        print ("~~*~~"*5)
        print (" Perimeter of Triangle is :\t", Perimeter)
        Triangle_Area.Display_Out_put(self)
        return round(self.area,2)

    def Display_input(self): # printing Input value
        print (" Result Without Using Parent Classs :")
        print ("~~*~~"*5)
        print (" 1st Side of Triangle is :\t",self.side_A)
        print (" 2nd Side of Triangle is :\t",self.side_B)
        print (" 3rd Side of Triangle is :\t",self.side_C)
        print ("~~*~~"*5)

    def Display_Out_put(self): # printing Area of Triangle
        print ()
        print (" Area of  Triangle  is    :\t",(round(self.area,2)))
        print ("~~*~~"*5)

""" Calling Class and Passing the Values """
Area_T = Triangle_Area(2,2,2)

Area_T.Area_caluation()

