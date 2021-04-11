# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 22:35:10 2021

@author: DELL
"""

import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist(r"pagerank.txt",create_using=nx.DiGraph(), nodetype=int)
nx.draw(G, with_labels=True)
plt.show()
result=nx.pagerank(G)
print(sorted(result.items(), key=lambda f:f[1]))