# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 16:07:25 2018

@author: jkdadhich
"""
Vowels = ['a','i','e','o','u'] # Declare Vowel

def Check_vowel(char): # Created function to check the vowels
    char = char.lower() # making or character in lower case
    for vowel in Vowels: # iterating over vowel defined
        if char == vowel: # Comparision if char equal to vowel
            return True # if yes return True
    return False # Not Matched False
print ("~~~*~~~"*10)
print ("Checking 'T' and 'A'")
print ("Result of 'T:\t", Check_vowel('T')) # Testing and printing the result
print ("Result of 'T:\t", Check_vowel('A')) # Testing and printing the result

""" This is just create for if Vowel present in word or not Using Simple way"""
# Word list defined
Word_list = ["summer","value","fly","sky","phd","pdf","cool"]
Word_list = [ X.lower() for X in Word_list ] # Making all words lower case
With_vowel = list(set([ word for word in Word_list for char in word if char in Vowels])) # Looping and getting only words which contains vowels in it
# Words which do not have any vowel character present
Not_vowel = [ word for word in Word_list if word not in With_vowel]

print ("~~~*~~~"*10)
print (" List of Words defined above :- ")
print (Word_list)
print ("~~~*~~~"*10)
print (" Words contain Vowel characters as per list :" )
print (With_vowel)
print ("~~~*~~~"*10)
print (" Words Not contain Vowel characters as per list :" )
print (Not_vowel)
print ("~~~*~~~"*10)


