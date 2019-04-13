#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:04:26 2019

@author: Alana
"""
'''
from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
movies = collection.getElementsByTagName(“movie")
for movie in movies:
    print('*****Movie*****')
    if movie.hasAttribute('title'):
        print('Title: ',movie.getAttribute('title'))
    type = movie.getElementsByTagName('type')[0]
    print('Type: ',type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print('Format: ',format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print('Rating: ',rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print('Description: ',description.childNodes[0].data)

common pattern in go_obo.xml
<term>
    <id>GO:XXXXXXX</id>
    <name>xxx</name>
    <def>
        <defstr>some_terms</defstr>
        <is_a>GO:XXXXXXX</is_a>
        <is_a>GO:XXXXXXX</is_a> #may have multiple parents
    <def>
</term>

element
 <term>
    <id>GO:0000002</id>
    <name>mitochondrial genome maintenance</name>
    <namespace>biological_process</namespace>
    <def>
      <defstr>The maintenance of the structure and integrity of the mitochondrial genome; includes replication and segregation of the mitochondrial chromosome.</defstr>
      <dbxref>
        <acc>ai</acc>
        <dbname>GOC</dbname>
      </dbxref>
      <dbxref>
        <acc>vw</acc>
        <dbname>GOC</dbname>
      </dbxref>
    </def>
    <is_a>GO:0007005</is_a>
 </term>
'''

count = 0
def create_global_variable():
    global count
    count = 0
    return count
create_global_variable()

from xml.dom.minidom import parse
import xml.dom.minidom
import panda as pd
import re
import numpy as np
dic = {'id':[],'name':[],'definition':[],'childnodes':[]}   
DOMTree = xml.dom.minidom.parse("go_obo.xml")    
obo = DOMTree.documentElement 
autophagosomes = obo.getElementByTagName('defstr')
for a in autophagosomes:
    if re.search ('autophagosome',autophagosomes):
       terms = autophagosomes.parentNode.parentNode
       ide = terms.getElementByTagName('id')[0].childNodes.data
       defstr = autophagosomes.data
       name = terms.getElementByTagName('name')[0].childNodes[0].data
       dic['id'].append(ide)
       dic['name'].append (name)
       dic['definition'].append (autophagosomes)
       for term in terms:
           parent_list = terms.getElementByTagName('is_a')
           for parent in parent_list:
               if parent.childnode[0].data == ide:
                  count = count + 1
                  count = count + 
                   

       