# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:53:56 2018

@author: jkdadhich
"""

# List of words
WORDs = ["Amazon","commerce","customer","information","Purchases"]
# function using swap the value to find longest word
def longest_word(list_words):
    if len(list_words) ==0 : # Check the passed list
        Message = "No Word Found in List"
        return Message # Return Message if empty list found
    max_word = list_words[0] # assign default postion
    for word in list_words: # iterating with list of words passed
        if len(max_word) < len(word): # Validating length
            max_word = word # if conditon true swap the new value to default postion defined above
    return (max_word) # printing longest word

# Simpliest way to do using lambda and max function
longest_word_2 = max(WORDs, key=lambda word: len(word))

# Lemman method to achive target (Not Suggest to use) but good for beginner to understand how to reterive the Longest word with basic learning
def Using_len_Index(WORDs):
    # Caluating length of Each words
    Length_of_element = [ len(x) for x in WORDs]
    # Taking Out Maximum Lenght Number
    max_value_ =  max(Length_of_element)
    # Getting address of maximum list
    max_value_adderess = Length_of_element.index(max_value_)
    # Fetching longest word using postion of max address reterive
    longest_WORD = WORDs[max_value_adderess]
    return (longest_WORD)

print ("~~*~~*"*15)
print (" First  Method : Longest_word     :\t",longest_word(WORDs))
print (" Second Method : Longest_word_2  :\t",longest_word_2)
print (" Third Method  : Using_len_Index :\t",(Using_len_Index(WORDs)))
print ("~~*~~*"*15)




