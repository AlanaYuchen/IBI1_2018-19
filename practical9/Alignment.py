#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 07:54:32 2019

@author: Alana
number1 = re.findall(r'[0-9]+',s)
"""
import re
dic={}
H = open('human.txt','r')
M = open('mouse.txt','r')
R = open('Random.txt','r')
h = H.read()
m = M.read()
r = R.read()
human = re.findall(r'[A-Z][A-Z][A-Z][A-Z]+',h)
mouse = re.findall(r'[A-Z][A-Z][A-Z][A-Z]+',m)
random = re.findall(r'[A-Z][A-Z][A-Z][A-Z]+',r)
hu = human[0]
mo = mouse[0]
ra = random[0]
edit_distance = 0
for i in range(0,len(hu)):
    if hu[i]!=mo[i]:
       edit_distance += 1 
print (edit_distance)    
      
edit_distance1 = 0
for i in range(len(hu)): #compare each amino acid
    if hu[i]!=ra[i]:
       edit_distance1 += 1 #add a score 1 if amino acids are
print (edit_distance1)
       
edit_distance2 = 0
for i in range(len(mo)): #compare each amino acid
    if ra[i]!=mo[i]:
       edit_distance2 += 1 #add a score 1 if amino acids are
print (edit_distance2)

B = open('BLOSUM62.txt','r')
b = B.readlines()

q = re.findall('[A-Z*]',b[0])
for i in range(0, len(q)):
    for j in range(1,len(b)): 
        v = int(b[j][3*i+2:3*i+4])        
        dic[(q[i],b[j][0])]=v
B.close()
l1=''
l2=''
l3=''
count1 = 0
count2 = 0
count3 = 0

score1 = 0
for i in range(0,len(hu)):
    if hu[i]!=mo[i]:
       l1 +='*'
    else:
        l1 += hu[i]
        count1 += 1
        print(count1)
    score1 += dic[(hu[i],mo[i])]
print('Human gene:',hu)
print('alignment:', l1)
print('Mouse gene:',mo)
print('The BLOSUM score of human and mouse:', score1)           
print('Similarity:', count1/len(hu)*100, '%')

score2 = 0
for i in range(0,len(hu)):
    if hu[i]!=ra[i]:
       l2 += '*'
    else:
        l2 += hu[i]
        count2 += 1
    score2 += dic[(hu[i],ra[i])]
print('Human gene:',hu)
print('alignment:', l2)
print('Random gene:',ra)
print('The BLOSUM score of human and random:', score2)  
print('Similarity:', count2/len(hu)*100, '%')

score3 = 0
for i in range(0,len(mo)):
    if mo[i]!=ra[i]:
       l3 += '*'
    else:
        l3 += mo[i]
        count3 += 1
    score3 += dic[(ra[i],mo[i])]
print('Random gene:',ra)
print('alignment:', l3)
print('Mouse gene:',mo)
print('The BLOSUM score of random and mouse:', score3)
print('Similarity:', count3/len(hu)*100, '%')       