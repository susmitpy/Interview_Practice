#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:12:28 2019

@author: susmitvengurlekar
"""

from collections import deque
from time import sleep

def all_routes(L,stacks,curr_route,routes,adj_list):
    print("Stacks: ", stacks)
    print("Routes: ", routes)
    print("Curr Route: ", curr_route)
    sleep(0.3)
    
    # All Routes Completed
    if len(stacks) == 0:
        return routes
    
    # One Brach Completed
    if len(stacks[-1]) == 0:
        stacks.pop()
        return all_routes(L,stacks,[curr_route[0]],routes,adj_list)
    
    nn = stacks[-1].pop()
    
    if nn not in curr_route:
        # Cannot visit one node twice
        curr_route.append(nn)
    else:
        return all_routes(L,stacks,curr_route,routes,adj_list)
    
    # Adding Children
    if len(adj_list[nn]) != 0:
        stack = deque()
        for i in adj_list[nn]:
            # Cannot visit one node twice
            if i not in curr_route:
                stack.append(i)
        stacks.append(stack)
        return all_routes(L,stacks,curr_route,routes,adj_list)
    
    
    if len(curr_route) == L:
        routes.append(curr_route)
    
    
    curr_route = curr_route[:-1]
    return all_routes(L,stacks,curr_route,routes,adj_list)
    

def main():
# =============================================================================
#     L = int(input())
#     N = int(input())
#     R = int(input())
#     C = int(input())
# =============================================================================
    L=7
    N=9
    R=9
    C=2
# =============================================================================
#     Adjacency List
#     CA = defaultdict(list)
#     for r in range(R):
#         t = [int(n) for n in input().split(" ")]
#         if t[1] not in CA[t[0]]:
#             CA[t[0]].append(t[1])
#         if t[0] not in CA[t[1]]:
#             CA[t[1]].append(t[0])
# =============================================================================
    CA={1: [4, 5, 7], 4: [1, 3, 6], 5: [1, 6], 7: [1, 6], 6: [5, 2, 4, 7], 2: [3, 6], 3: [2, 4]}
    stacks = []
    routes = []
    
    for k in CA.keys():
        stack = deque(CA[k])
        stacks.append(stack)
        routes = all_routes(L,stacks=stacks,curr_route=[k],routes=routes,adj_list=CA)
        print(routes)
        break  # Till Now
    
main()