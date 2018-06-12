# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:32:56 2018

@author: jkdadhich
"""
# User defined lsit
List = ["python","Machine","Demo","Class","physic","maths"]

Result = [ len(x) for x in List] # Using Just lenght while iterating the words

# Here Making User base interface for same kind of problem
# How many time you insert the words (Use interger only)
Input_int = int(input("Tell Us how many times you will enter word :\t "))
Start = 1 # Setting Count by default as One Entry

List_of_Words = [] # Word will be append in this empty list
while Start <= Input_int: # While checking or count for entry
    Word = str(input("Please Enter the your {} word :\t".format(Start))) # Enter you word here
    List_of_Words.append(Word) # appending the list
    Start = Start+1 # Counter reset with increment by 1

Result_2 = list(map(lambda x : len(x), List_of_Words)) # Using map and lamba getting lenght of word

print ("~~*~~"*5)
print (" User Defined list :\n")
print (List)
print (" Lenght of Words present in Above list:")
print (Result) # Result will be list of lenght of words
print ("~~*~~"*5)
print (" User Interaface List of Words :\n")
print (List_of_Words)
print (" Lenght of Words present in Above list:")
print (Result_2)  # Result will be list of lenght of words
print ("~~*~~"*5)


