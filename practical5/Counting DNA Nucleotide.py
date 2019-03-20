#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:33:21 2019

@author: chenghui
"""

L = 'ATGCTTCAGAAAGGTCTTACG'  
A = 0
T = 0
G = 0
C = 0
for index in range (len(L)):
    if L[index]=='A':
        A = A+1
    elif L[index]=='T':
        T = T+1
    elif L[index]=='G':
        G = G+1
    else:
        C = C +1
nt = len(L)
percentA = A/nt*100
percentT = T/nt*100
percentG = G/nt*100
percentC = C/nt*100
import matplotlib.pyplot as plt
labels = 'A', 'T', 'G', 'C'
sizes = [percentA, percentT, percentG, percentC]
plt.pie(sizes, labels=labels,shadow=False, startangle=90, autopct='%1.1f%%')
plt.title ('pie of the four DNA nucleotide')
plt.axis('equal')
plt.show()