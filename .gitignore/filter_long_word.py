# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:20:02 2018

@author: jkdadhich
"""

def Filter_Long_Words(words,Long_n):

    return list(filter(lambda x : len(x)> Long_n,words))

Words_List = ["Junior","Senior","word","jump","python","Heroic"]

Result_Long_Word = Filter_Long_Words(Words_List,4)

print ("~~*~~"*10)
print (" Word List Defined :~~\n","~*~"*10,"\n",Words_List)
print ("~~*~~"*10)
print (" list of words have characters > 4 :~~\n","~*~"*10,"\n",Result_Long_Word)
print ("~~*~~"*10)
