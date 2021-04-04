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


'''
Consider a directed graph. It can be represented by an adjacency matrix. The nodes are numbered 1 to n. If there is an edge from node i to node j, there will be a 1 in the (i-1,j-1) position in the adjacency matrix. There are no self loops in the graph. For a node, the number of head ends adjacent to a node is called the indegree of the node and the number of tail ends adjacent to a node is its outdegree. Print 'yes'  and the node number if  in the given graph there is a node with indegree 2, else print 'no'. Adjacency matrix is given as a line of zeros and ones in row major order i.e, row 1 will be given as input first then the row 2 so on. There will be only one edge with indegree 2.

Input format :
Line 1 - Number of nodes
Line 2 - Adjacency matrix in row major order

Output format : if the condition is satisfied then yes node_number else no

Example 
input:
4
0 1 0 0 0 0 0 1 1 0 0 0 0 1 0 0
output
no

'''
import numpy as np
node=int(input())
flag = 0
count = 0
a=[int(x) for x in input().split()]
print(a)
matrix = np.array(a).reshape(node,node)
print(matrix)
for row in matrix:
    count = count + 1
    print(count)
    temp=np.array(row).tolist()
    print(temp)
    if temp.count(1) == 2:
        print('yes', count)
        flag = 1
if flag == 0:
    print('no')

'''
Consider a directed graph. It can be represented by an adjacency matrix. The nodes are numbered 1 to n. If there is an edge from node i to node j, there will be a 1 in the (i-1,j-1) position in the adjacency matrix. There are no self loops in the graph. For a node, the number of head ends adjacent to a node is called the indegree of the node and the number of tail ends adjacent to a node is its outdegree. Print 'yes'  and the node number if  in the given graph there is a node with outdegree 2, else print 'no'. Adjacency matrix is given as a line of zeros and ones in row major order i.e, row 1 will be given as input first then row 2 so on. There will be only one edge with outdegree 2.


Input format :

Line 1 - Number of nodes

Line 2 - Adjacency matrix in row major order


Output format : if the condition is satisfied then yes node_number else no


Example 

input:

4
0 1 0 0 0 0 0 1 1 0 0 0 0 1 0 

output

yes 2
'''
import numpy as np
node=int(input())
flag = 0
count = 0
a=[int(x) for x in input().split()]
print(a)
matrix = np.array(a).reshape(node,node)
print(matrix)
matrix=(matrix.T)
print(matrix)
for column in matrix:
    count = count + 1
    print(count)
    temp=np.array(column).tolist()
    print(temp)
    if temp.count(1) == 2:
        print('yes', count)
        flag = 1
if flag == 0:
    print('no')

'''
Consider a directed graph. It can be represented by an adjacency matrix. The nodes are numbered 1 to n. If there is an edge from node i to node j, there will be a 1 in the (i-1,j-1) position in the adjacency matrix. There are no self loops in the graph. print yes if the given graph is a complete graph (connection from one node to all other node) else print no
'''
import numpy as np
node=int(input())
count = 0
a=[int(x) for x in input().split()]
matrix = np.array(a).reshape(node,node)
for row in matrix:
 temp=np.array(row).tolist()
 if temp.count(1) == node-1:
  count = count+1
 
if count == node:
 print('yes')
else:
 print('no')
 
 
 # When our graph will be undirected, then it will be symmetric as well.
 # self loop means  (0,0),(1,1) and all
 # directed graph(1,2), (2,5)  ,1-->2 , 2-->5
 # undirected graph {1,2},{3,4}, 1--2, 3--5