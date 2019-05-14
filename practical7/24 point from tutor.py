#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:20:21 2019

@author: chenghui
"""
import re
from fractions import Fraction
t=0
numbers = input ("Please input numbers to computer 24(use ',' to divide them):\n")
l = re.split(',',numbers)
l = list(map(eval, l))# turn the numbers into a list
for i in l:
    if i%1!=0 or i<1 or i>23:
       print('The input number must be integers from 1 to 23')
       numbers = input ("Please input numbers to computer 24(use ',' to divide them):")
       t=t+1
       break
    elif t==len(l)-1:
        print ('Yes')
        break
    else:
        t=t+1
        continue
n = len(l)

count = 0
solution = 0
def dfs(n):
    global count
    global solution
    count = count + 1
    
    if n == 1:
        if (float (l[0])==24):
            solution = solution+1
            return 1
        else:
            return 0
    for i in range (0,n):
        for j in range (i+1,n):
            a = l[i]
            b = l[j]
            l[j] = l[n-1]
            
            l[i] = a+b
            if (dfs(n-1)):
                return 1
            l[i] = a*b
            if (dfs(n-1)):
                return 1
            
            if a :
                l[i] = Fraction(a,b)
                if (dfs(n-1)):
                    return 1
            l[i] = a
            l[j] = b
        return 0
if (dfs(len(l))):
    print('Yes')
else:
    print('No')
print('Recursion times:',count,', Solution:',solution)
                
              