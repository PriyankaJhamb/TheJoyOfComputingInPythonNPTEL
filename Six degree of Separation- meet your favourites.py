# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:05:57 2021

@author: Priyanka
"""

import networkx as nx
import numpy

G=nx.read_edgelist("facebook_combined.txt")

#compare the lenght of shortest path between each pair of nodes possible

N=list(G.nodes())

spll=[]#shortest path linked list

for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G, u, v)
            print("Shortest path between:",u,"and",v,"if of length",l)
            spll.append(l)
            
min_spl=min(spll)#minimum shortest path length
max_spl=max(spll)
avg_spl=numpy.average(spll)

print("Minimum shortest path length:",min_spl)
print("Maximum shortest path length:",max_spl)
print("Average shortest path length:",avg_spl)