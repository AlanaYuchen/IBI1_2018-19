#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:43:09 2019

@author: Alana
"""
import numpy as np
import matplotlib.pyplot as plt
Susceptible = 9999
Infected = 1
Recovered = 0
N = 10000
beta = 0.3
gamma = 0.05
S = []
I = []
R = []
S.append(Susceptible)
I.append(Infected)
R.append(Recovered)
for a in range (0,1000):
    infect = 0
    recover = 0
    m = np.random.choice(range(2),Susceptible,p=[1-beta*Infected/N,beta*Infected/N])
    for i in m:
        if i == 1:
           infect += 1
    n = np.random.choice(range(2),Infected,p=[1-gamma,gamma])
    for j in n:
        if j == 1:
           recover += 1
    Susceptible = Susceptible - infect
    Infected = Infected + infect - recover
    Recovered += recover
    S.append(Susceptible)
    I.append(Infected)
    R.append(Recovered)
#--------------------------------plot------------------------------------------
x = np.linspace(0, 1000, 1001)
plt.plot(x, S,label = 'Susceptible')    
plt.plot(x, I,label = 'Infected') 
plt.plot(x, R,label = 'Recovered')     
plt.xlabel('times')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.show()
plt.figure(figsize=(6,4),dpi=150)
plt.savefig("SIR model",type="png")

