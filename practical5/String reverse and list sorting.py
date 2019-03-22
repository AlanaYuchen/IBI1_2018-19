#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:36:35 2019

@author: chenghui
"""
#method 1
words = 'learning python is exhausting but interesting'
splited_words=words.split (' ')
# a new list need to be created to srote mutated letters!
new_words=[]
for letter in splited_words:
    splited_words = splited_words
    letter = letter[::-1]
    new_words.append(letter)
# sort: arrange the words alphebetical order
# reserve: reserve the sequence of elements  
new_words.sort()
new_words.reverse() 
print (new_words)

#method 2
words = 'learning python is exhausting but interesting'
splited_words=words.split (' ')
#amazing methods!
for letter in range (len(splited_words)):
    splited_words[letter] = splited_words[letter][::-1]
splited_words.sort()
splited_words.reverse()
print (splited_words)  
  
#using 'input' to make it more easy to use!
words = input('give me a string of words :' )
splited_words=words.split (' ')
for letter in range (len(splited_words)):
    splited_words[letter] = splited_words[letter][::-1]
splited_words.sort()
splited_words.reverse()
print (splited_words)  

#lessen the codes  
words = input('give me a string of words :' )
splited_words=words.split (' ')
for letter in range (len(splited_words)):
    splited_words[letter] = splited_words[letter][::-1]
splited_words.sort(reverse=True)
print (splited_words)  