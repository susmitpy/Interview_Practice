#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:35:32 2019

@author: susmitvengurlekar
"""

from collections import defaultdict 
from collections import deque
from time import sleep




#Class to represent a graph 
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary  
                                # to store graph 
          
   
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
  
    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    # The main function to construct MST using Kruskal's  
        # algorithm 
    def KruskalMST(self): 
  
        result =[] #This will store the resultant MST 
  
        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 
  
            # Step 1:  Sort all the edges in non-decreasing  
                # order of their 
                # weight.  If we are not allowed to change the  
                # given graph, we can create a copy of graph 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 
  
            # Step 2: Pick the smallest edge and increment  
                    # the index for next iteration 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            # If including this edge does't cause cycle,  
                        # include it in result and increment the index 
                        # of result for next edge 
            if x != y: 
                e = e + 1     
                result.append([u,v]) 
                self.union(parent, rank, x, y)             
            # Else discard the edge 
  
        # print the contents of result[] to display the built MST 
        #print ("Following are the edges in the constructed MST")
        self.result = result
# =============================================================================
#         for u,v  in result: 
#             #print str(u) + " -- " + str(v) + " == " + str(weight) 
#             print ("%d -- %d" % (u+1,v+1)) 
# =============================================================================
  
# Driver code 
g = Graph(7) 

CA={1: [4, 5, 7], 4: [1, 3, 6], 5: [1, 6], 7: [1, 6], 6: [5, 2, 4, 7], 2: [3, 6], 3: [2, 4]}

for i,j in CA.items():
    for dest in j:
        g.addEdge(i-1,dest-1,1)


  
g.KruskalMST() 

 
adj_list = defaultdict(list)

ed = g.result
l = len(ed)



for i in range(l):
    if ed[i][0] not in adj_list[ed[i][1]]:
         adj_list[ed[i][1]].append(ed[i][0])

    if ed[i][1] not in adj_list[ed[i][0]]:
         adj_list[ed[i][0]].append(ed[i][1])

print(adj_list)

    


