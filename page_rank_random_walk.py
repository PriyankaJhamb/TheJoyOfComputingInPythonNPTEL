# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:42:52 2021

@author: DELL
"""

# Drunkird's Walk 
# Random Walk
# Crawlers take random walk on www network and rank the websites.
# It does not only matter that how many number of votes one has got but what the more matters is who is refering.

import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

G=nx.gnp_random_graph(10,0.5, directed=True)
nx.draw(G, with_labels=True)

# x is the random source code
x=random.choice([i for i in range(nx.number_of_nodes(G))])

dict_counter={}

for i in range(nx.number_of_nodes(G)):
    dict_counter[i]=0
    
dict_counter[x]=dict_counter[x]+1
for i in range(1000000):
    list_n=list(G.neighbors(x))
    if(len(list_n)==0):  #if a node is a sink
        x=random.choice([i for i in range(nx.number_of_nodes(G))])
    else:
        x=random.choice(list_n) # choose a node from the neighbors
        dict_counter[x]=dict_counter[x]+1
        
p=nx.pagerank(G)
sorted_p=sorted(p.items(), key=operator.itemgetter(1))#itemgetter(1 if you want on the basis of value and 0 of you want on the basis of keys)
sorted_rw=sorted(dict_counter.items(), key=operator.itemgetter(1))
print(sorted_p)
print(sorted_rw)
# print(sorted(p.items(),key=lambda f:f[1]))
# print(sorted(dict_counter.items(),key=lambda f:f[1]))    












 