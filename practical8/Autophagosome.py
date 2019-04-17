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



def child (parent_list, resultset):
    for parent in parent_list:
        if parent.childNodes[0].data == ide:
           resultset.add(geneid) 
           child (geneid,resultset)
           
import xml.dom.minidom
import pandas as pd
import re

dic = {'id':[],'name':[],'definition':[],'childnodes':[]}   
DOMTree = xml.dom.minidom.parse("go_obo.xml")    
c = DOMTree.documentElement 
autophagosomes = c.getElementsByTagName('defstr')
for a in autophagosomes:
    auto = a.childNodes[0]
    if re.search ('autophagosome',auto.data):
       terms = auto.parentNode.parentNode.parentNode
       ide = terms.getElementsByTagName('id')[0].childNodes[0].data
       name = terms.getElementsByTagName('name')[0].childNodes[0].data
       autod = auto.data
       parent_list = terms.getElementsByTagName('is_a')
       geneid = terms.getElementsByTagName('id')[0].childNodes[0].data
       for parent in parent_list:
           resultset = set('')
           child (parent_list, resultset)
       children = len(resultset)
       dic['id'].append(ide)
       dic['name'].append (name)
       dic['definition'].append (autod)
       dic['childnodes'].append(children)
               
dt = pd.DataFrame(dic)
dt.to_excel('autophagosome1.xlsx', sheet_name='Sheet1')               
               

                       

       