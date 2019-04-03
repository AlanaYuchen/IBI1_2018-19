#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:22:48 2019

@author: Alana
"""
#----------------------input an integer between 1 and 23-----------------------
import re
t=0
numbers = input ("Please input numbers to computer 24(use ',' to divide them):")
numberlist = re.split(',',numbers)
print(numberlist)
numberlist = list(map(eval, numberlist))
for i in numberlist:
    if (i%2!=0 and i%2!=1) or (i/2<=0.5 and i/2>12):
       print('The input number must be integers from 1 to 23')
       numbers = input ("Please input numbers to computer 24(use ',' to divide them):")
       t=t+1
       break
    elif t==len(numberlist)-1:
        print ('Yes')
        break
    else:
        t=t+1
        continue

       
