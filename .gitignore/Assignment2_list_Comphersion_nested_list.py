# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:27:42 2018

@author: jkdadhich
"""

Text = "acadgild"

Result = [x.upper() for x in Text] # Using Uppercase and iterate over character

Variable = "xyz"

# Mulitpy iteration with range
Result_1 = [ x*k for x in Variable for k in range(1,5)]

# mulitply range with iterator item
Result_2 = [ k*d for k in range(1,5) for d in Variable]

# Iteration over range creating list of list
Result_3 = [[i+j] for j in range(0,3) for i in range(2,5)]

# but as above change the input seq. as result
Result_4 = [[i+j for j in range(0,4)] for i in range(2,6)]
# nested loop over range store as outer as list inside as tuple
Result_5 = [(i,j) for j in range(1,4) for i in range(1,4)]

print ("~*~"*15)
print (Result)
print ("~*~"*15)
print (Result_1)
print ("~*~"*15)
print (Result_2)
print ("~*~"*15)
print (Result_3)
print ("~*~"*15)
print (Result_4)
print ("~*~"*15)
print (Result_5)
print ("~*~"*15)

