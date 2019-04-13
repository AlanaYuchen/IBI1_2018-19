#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:32:20 2019

@author: Alana
"""
#http://geneontology.org/docs/ontology-documentation/
#http://pandas.pydata.org/pandas-docs/stable/
"""
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

from GO homepage:
    "The structure of GO can be described in terms of a graph, where each GO term is a node, and the relationships between the terms are edges between the nodes. 
    GO is loosely hierarchical, with ‘child’ terms being more specialized than their ‘parent’ terms, 
    but unlike a strict hierarchy, a term may have more than one parent term (note that the parent/child model does not hold true for all types of relations, see the relations documentation). 
    For example, the biological process term hexose biosynthetic process has two parents, hexose metabolic process and monosaccharide biosynthetic process. 
    This reflect the fact that biosynthetic process is a subtype of metabolic process and a hexose is a subtype of monosaccharide."
      
"""

import xml.dom.minidom
import pandas as pd
import re


DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement

#tms = collection.getElementsByTagName('term')
nodes = collection.getElementsByTagName('defstr') 
is_a = collection.getElementsByTagName('is_a') 

"""
def child(x): #x is a text string
    count = 0
    for tm in tms:
        is_a = tm.getElementsByTagName('is_a')
        for isa in is_a:
            if x == isa.childNodes[0].data:
                count += 1
                count += child(tm.getElementsByTagName('id')[0].childNodes[0].data)
            return count
"""
dic = {'id':[],'name':[],'definition':[],'childnodes':[]}
res = set('')
def child(x,res):
    for j in range(0, is_a.length):
        if x == is_a[j].childNodes[0].data:
            iden = is_a[j].parentNode.getElementsByTagName('id')[0].childNodes[0].data
            res.add(iden)
            child(iden,res)
    
for i in range(0, nodes.length):
    defelm = nodes[i].childNodes[0]
    if re.search('autophagosome', defelm.data):
        term = defelm.parentNode.parentNode.parentNode #parent of the defstr element is <defstr> node
        ide = term.getElementsByTagName('id')[0].childNodes[0].data
        defstr = defelm.data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        child(ide,res)
        children = len(res)
        res = set('')
        dic['id'].append(ide)
        dic['name'].append(name)
        dic['definition'].append(defstr)
        dic['childnodes'].append(children)
        #use a function to find number of childnodes



dt = pd.DataFrame(dic)
dt.to_excel('autophagosome.xlsx', sheet_name='Sheet1')

    