#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 08:32:36 2019

@author: chenghui
"""
a = 425
b = 425425
b % 7
c = b / 7
d = c / 11
e = d / 13
print (e)

X = True
Y = True
Z = (X and not Y) or (Y and not X)
W = X != Y
if (Z == W):
    print ("True")
else:
    print ("False")

X = True
Y = False
Z = (X and not Y) or (Y and not X)
W = X != Y
if (Z == W):
    print ("True")
else:
    print ("False")
    
X = False
Y = True
Z = (X and not Y) or (Y and not X)
W = X != Y
if (Z == W):
    print ("True")
else:
    print ("False")
  
X = False
Y = False
Z = (X and not Y) or (Y and not X)
W = X != Y
if (Z == W):
    print ("True")
else:
    print ("False")
    
    
