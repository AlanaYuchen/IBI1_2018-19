#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:30:03 2019

@author: chenghui
"""

x = 1733
output = str(x) + ' is '
#find the largest number of 2**n but is smaller than x
n=13
while x!= 0:
    if 2**n > x:
        n=n-1
    else:
        x = x-2**n
        if x !=0:
           output= output + '2**' + str(n) + ' + ' 
        else:
            output= output + '2**' + str(n) 
print (output)
    


    