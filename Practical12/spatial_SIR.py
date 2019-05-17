#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:14:11 2019

@author: Alana
"""

import numpy as np
import matplotlib.pyplot as plt
# make array of all susceptible population
population = np.zeros((100,100)) 
#randomly choose one cell and infected it by turning the value into 1
outbreak = np.random.choice(range(100),2) 
population[outbreak[0],outbreak[1]]=1
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap='viridis',interpolation = 'nearest')
beta = 0.3
gamma = 0.05

'''
pseudocode:
    
create a dictionary to store the position of eight neighbours of a cell (infected person).
    
excute 100 times
for each time
find the infected people
use np.random.choice to simulate whether they can recover (if so turn the value into 0.5)

find the cells that are still infected 
for 8 neighbours, use np.random.choice to simulate whether they can be infected, use 1 to represent the people being infected.
if 1 exists and is within the range of 100*100 array, use index to fetch the real position of that person and infected him/her
create a plot after each excution
'''

dic={0:(-1,-1),1:(-1,0),2:(-1,1),3:(0,1),4:(1,1),5:(1,0),6:(1,-1),7:(0,-1)}

for a in range(0,100): # try to recover
    I = np.where(population==1)
    for i in range(0,len(I[0])):
        recover = np.random.choice(range(2),1,p = [1-gamma,gamma])
        if recover == 1:
           population[I[0][i],I[1][i]]=0.5
           
    inf = np.where(population==1) #try to infect
    for j in range(0,len(inf[0])):
        infected = np.random.choice(range(2),8,p=[1-beta,beta])
        for m in range(0,len(infected)):
            try:
                if infected[m] == 1 and population[dic[m][0]+inf[0][j],dic[m][1]+inf[1][j]] != 0.5 and dic[m][0]+inf[0][j]>=0 and dic[m][1]+inf[1][j]>=0:
                   population[dic[m][0]+inf[0][j],dic[m][1]+inf[1][j]]= 1
            except:
                pass
    plt.figure(figsize=(6,4),dpi=150)
    plt.imshow(population, cmap='viridis',interpolation = 'nearest')
