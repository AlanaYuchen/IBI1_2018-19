#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:22:48 2019

@author: Alana
"""

count = 1

def create_global_variable():
    global count
    count = 0
    return count
create_global_variable()
print (count)

#----------------------input an integer between 1 and 23-----------------------

import re
t=0
numbers = input ("Please input numbers to computer 24(use ',' to divide them):")
l = re.split(',',numbers)
l = list(map(eval, l))
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
l = [l]

#-----------------------calculate 24 point-------------------------------------

from operator import mul, sub, add


def div(a, b):
    if b == 0:
        return 999999.0
    return a / b


ops = {mul: '*', div: '/', sub: '-', add: '+'}
count = 0
def solve24(num, how, target):
    global count
    if len(num) == 1:
        if round(num[0], 5) == round(target, 5):
            yield str(how[0]).replace(',', '').replace("'", '')
            count += 1
    else:
        for i, n1 in enumerate(num):
            for j, n2 in enumerate(num):
                if i != j:
                    for op in ops:
                        new_num = [n for k, n in enumerate(num) if k != i and k != j] + [op(n1, n2)]
                        new_how = [h for k, h in enumerate(how) if k != i and k != j] + [(how[i], ops[op], how[j])]
                        yield from solve24(new_num, new_how, target) 
                        count += 1
    return count
for nums in l:  
    print(nums, end=' : ')
    try:
        print(next(solve24(nums, nums, 24)))
        print ('Recursive times:', count)
    except StopIteration:
        print("No solution found")
       
