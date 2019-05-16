#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:10:41 2019

@author: Alana
"""

import os
import numpy as np
import xml.dom.minidom
import re
import random
import matplotlib.pyplot as plt

os.chdir('/Users/chenghui/Documents/IBI1/GitKraken/IBI1_2018-19/Practical13')
data = {'maximumpredator' : [], 'minimumpredator' : [],'k_predator_breeds':[],'k_predator_dies':[],'k_prey_breeds':[],'k_prey_dies':[]}
# the function used to convert xml into cps
def xml_to_cps():
    
    # first, convert xml to cps 
    os.system("/Applications/COPASI/CopasiSE -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w")
    cpsTree.writexml(cpsFile)
    cpsFile.close()


#run copasi in python
os.system("/Applications/COPASI/CopasiSE predator-prey.cps")
r = open('modelResults.csv', 'r').readlines() 
name = r[0]
names = name.split(',')
result = r[1:]
results = []
for line in result:
    l = line.split(',')
    results.append(l)
results = np.array(results)  
results = results.astype(np.float)  


#plot a time course for predator prey    
plt.plot(results[:,0], results[:,1],label = 'Predator (b=0.02, d=0.4)')    
plt.plot(results[:,0], results[:,2],label = 'Prey (b=0.1, d=0.02)')    
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend()
plt.show()
# plot predator population against prey population
plt.plot(results[:,1], results[:,2])    
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('LImit cycle')
plt.show()

    
#------------------------------step 5------------------------------------------   
for i in range (0,50):
    k_predator_breeds = random.random()#pick random number between 0 and 1
    k_predator_dies =  random.random()
    k_prey_breeds = random.random()
    k_prey_dies = random.random()
        
    DOMTree = xml.dom.minidom.parse("predator-prey.xml")  # parse the XML file into a DOM document object  
    c = DOMTree.documentElement 
    parameters = c.getElementsByTagName('parameter')
    for parameter in parameters:
        att = parameter.getAttribute('id')
        if re.match ('k_predator_breeds',att):
           parameter.setAttribute('value', str(k_predator_breeds))
        if re.match ('k_predator_dies',att):
           parameter.setAttribute('value', str(k_predator_dies))
        if re.match ('k_prey_breeds',att):
           parameter.setAttribute('value', str(k_prey_breeds))
        if re.match ('k_prey_dies',att):
           parameter.setAttribute('value', str(k_prey_dies))
    filexml = open('predator-prey.xml','w')
    DOMTree.writexml(filexml)
    filexml.close()
    data['k_predator_breeds'].append(k_predator_breeds)
    data['k_predator_dies'].append(k_predator_dies)
    data['k_prey_breeds'].append(k_prey_breeds)
    data['k_prey_dies'].append(k_prey_dies)
    xml_to_cps()
    os.system("/Applications/COPASI/CopasiSE predator-prey.cps")
    r = open('modelResults.csv', 'r').readlines() 
    name = r[0]
    names = name.split(',')
    result = r[1:]
    results = []
    for line in result:
        l = line.split(',')
        results.append(l)
    results = np.array(results)
    results = results.astype(np.float)
    maxipredator = results[:,1].max() 
    minipredator = results[:,2].min()
    data['maximumpredator'].append(maxipredator)
    data['minimumpredator'].append(minipredator)
    plt.plot(results[:,0], results[:,1],label = 'Predator (b='+ str(k_predator_breeds)+ ', d=' + str(k_predator_dies)+')')    
    plt.plot(results[:,0], results[:,2],label = 'Prey (b='+ str(k_prey_breeds)+ ', d=' + str(k_prey_dies)+')')    
    plt.xlabel('time')
    plt.ylabel('population size')
    plt.title('Time course')
    plt.legend()
    plt.show()


#-----------------------------task 6-------------------------------------------
'''
1. Create a dictionary (with array) to store the results of each simulation.
2. The results included:
    The maximun and minimun of predator & prey population size.
    Oscillation period of predator & prey.
3. Analyze the data to see whether there are relationships between parameters, population sizes and oscillation periods (e.g. dot plot).
or can further uses some functions similar to 'parameter scan' in COPASI. 
'''
plt.scatter(data['k_predator_breeds'],data['maximumpredator'])
plt.xlabel('predator breeds rate')
plt.ylabel('maximum predator size')
plt.title('predator breeds rate ~ maximum predator size')
#more plot could be created