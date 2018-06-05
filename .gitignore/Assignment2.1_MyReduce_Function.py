# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:35:10 2018

@author: jkdadhich
"""

Element_Pass = [11,42,13,40,45,50,15,61,45,69]

def MY_Reduce_function(func, iterable):
    if len(iterable) == 0: # Validating the len of In put task
        return []

    result = iterable[0]

    for i in range(1, len(iterable)): # looping iterable
        result = func(result,iterable[i]) # function applied over iterating values
    return result



Result_Reduce = MY_Reduce_function(lambda x,y: x+y, Element_Pass)


def myfilter(func, elem_list):
    output = [] # Empty list to update the results and return in this function
    for elem in elem_list:
        if func(elem) == True: # validating the conditon function passes
            output.append(elem)
    return output

Result_Filter = myfilter(lambda x: x > 15, Element_Pass)

print ("~*~"*15)
print (" List for testing Results :")
print (Element_Pass)
print ("~*~"*15)
print (" Reduce function over list calulating sum of numbers :")
print (" Result_Reduce :\t", Result_Reduce)
print ("~*~"*15)
print (" Filter function over list calulating Greater than 15 :")
print (" Result_Filter :\t", Result_Filter)
print ("~*~"*15)