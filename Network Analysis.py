# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:18:05 2021

@author: DELL
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
#to add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

l=[4,5,6]
G.add_nodes_from(l)
#add edges # undirected edge
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)
print(G.nodes())
print(G.edges())

print(G.degree())
nx.draw(G)
# plt.show()


#scale free graph
O=nx.barabasi_albert_graph(50,2)#(nodes, a node coming with 2 edges and attach with the element have higher degree)
nx.write_gexf(O, "network_analysis.gexf")
# then opene Gephi tool(application used to visualize the graph) required java 1.8 
'''
M=nx.complete_graph(10)
nx.draw(M)

#random graphs
N=nx.gnp_random_graph(20,0.5)#(Node, probability)
nx.draw(N)

'''