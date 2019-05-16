#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 07:54:32 2019

@author: Alana
number1 = re.findall(r'[0-9]+',s)
"""
#------------------read the txt file with gene names---------------------------
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

#----------------calculate the Hamming distance--------------------------------
edit_distance = 0
for i in range(0,len(hu)):#compare each amino acid
    if hu[i]!=mo[i]:
       edit_distance += 1 #add a score 1 if amino acids are
print (edit_distance)    
      
edit_distance1 = 0
for i in range(len(hu)): 
    if hu[i]!=ra[i]:
       edit_distance1 += 1 
print (edit_distance1)
       
edit_distance2 = 0
for i in range(len(mo)): 
    if ra[i]!=mo[i]:
       edit_distance2 += 1 
print (edit_distance2)

#------------------read a txt file of BLOSUM62 into a dictionary---------------
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
    score1 += dic[(hu[i],mo[i])]
print('Human gene:',hu)
print('alignment:', l1)
print('Mouse gene:',mo)
print('The BLOSUM score of human and mouse:', score1)           
print('Normalized BLOSUM score:',score1/len(hu))
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
print('Normalized BLOSUM score:',score2/len(hu))
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
print('Normalized BLOSUM score:',score3/len(mo))
print('Similarity:', count3/len(hu)*100, '%')



#========================try to define a function==============================
def s (seq1,seq2,count, score):
    l=''
    count=0
    score=0
    for i in range(0,len(seq1)):
        if seq1[i]!=seq2[i]:
            l +='*'
        else:
            l+=seq1[1]
            count += 1
        score += dic[(seq1[i],seq2[i])]
    print('sequence1:', seq1)
    print('alignment:',l)
    print('sequence2:', seq2)
    print('The BLOSUM score of seq1 and seq2:', score)
    print('Normalized BLOSUM score:',score/len(seq1))
    print('Similarity:', count/len(seq1)*100, '%') 

s (mo,ra,count1,score1) 
s (hu,mo,count2,score2)
s (hu,ra,count3,score3)   