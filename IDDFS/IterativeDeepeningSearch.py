# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:13:45 2020

@author: Arpana M R
"""

from collections import defaultdict


class IDDFS:
    
    def __init__(self,vertices):
        
        self.v=vertices
        self.graph=defaultdict(list)
        
    def newEdge(self,u,v):
        self.graph[u].append(v)
        
    def DepthLimitSearch(self,src,dest,maxiDepth):
        
        if src==dest:
            return True
        
        if maxiDepth<=0:
            return False
        
        for i in self.graph[src]:
            if(self.DepthLimitSearch(i, dest, maxiDepth-1)):
                return True
        
        return False
    
    
    def IterDeepeningSearch(self,src,dest,maxiDepth):
        
        for i in range(maxiDepth):
            if self.DepthLimitSearch(src, dest, i):
                return True
        return False
    
    
n=int(input("Enter number of Vertices"))
G=IDDFS(n)

m=int(input("Enter number of edges"))
while m:
    print("Enter vertices u,v such that u-v is an edge")
    u,v=map(int,input().split())
    G.newEdge(u, v)
    m-=1

start=int(input("Enter Start node"))
des=int(input("Enter Destination node"))
Depth=int(input("Enter maximum possible depth to traverse"))

if G.DepthLimitSearch(start,des,Depth) == True:
    print("The destination is reachable from source within given max depth")
else:
    print("The destination is not reachable from source within given max depth")