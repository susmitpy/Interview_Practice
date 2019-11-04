#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:41:43 2019

@author: susmitvengurlekar
"""

from time import sleep
from collections import deque
# =============================================================================
# adj_list={1:[2,3],2:[4,5],3:[6,7],4:[],5:[],6:[],7:[]}
# 
# stack = deque()
# routes = []
# 
# def push_children(adj_list, stack, routes,curr_route,links_remaining):
#     sleep(0.3)
#     print("Function Called")
#     print("Stack: ", stack)
#     print("Routes: ", routes)
#     print("Curr Route: ",curr_route)
#     print("Links: ",links_remaining)
#     
# 
#     
#     
#     if links_remaining == 0:
#         if type(stack[-1]) == str:
#             return routes
#         if len(stack) == 0 or len(stack) == 1:
#             return routes
#         stack.pop()
#         return push_children(adj_list,stack,routes,curr_route[:-1],1)
#     if type(stack[-1])==str:
#         stack.pop()
#     curr_route.append(stack[-1])
#  
# 
#     if len(adj_list[curr_route[-1]]) != 0:
#         stack.append(str(len(adj_list[curr_route[-1]])))
#         for next_node in adj_list[curr_route[-1]]:
#             stack.append(next_node)
#             
#         print("Children Added")
#         print("Stack: ", stack)
#         return push_children(adj_list,stack,routes,curr_route,len(adj_list[curr_route[-1]]))
#     
#     print("One Path Complete")
#     
#     routes.append(curr_route)    
#     curr_route = curr_route[:-1]
#     stack.pop()
#     
#     print("Routes: ", routes)
#     print("Stack: ", stack)
#     
#     
#     print("In middle of a branch")
#     return push_children(adj_list,stack,routes,curr_route,links_remaining-1)
#     
# 
# for src in adj_list.keys():
#     stack.append(src)
#     routes = push_children(adj_list,stack,routes,[],len(adj_list[src]))
#     print(f"Routes: {routes}")
#     break
#     
# =============================================================================


def all_routes(L,src,stacks,curr_route,routes,adj_list):
    print("Stacks: ", stacks)
    print("Routes: ", routes)
    print("Curr Route: ", curr_route)
    
    # All Routes Completed
    if len(stacks) == 0:
        return routes
    
    if len(stacks[-1]) == 0:
        stacks.pop()
        return all_routes(L,src,stacks,[curr_route[0]],routes,adj_list)
    
    nn = stacks[-1].pop()
    
    if nn not in curr_route:
        curr_route.append(nn)
    else:
        return all_routes(L,src,stacks,curr_route,routes,adj_list)
    
    if len(adj_list[nn]) != 0:
        stack = deque(adj_list[nn])
        stacks.append(stack)
        return all_routes(L,src,stacks,curr_route,routes,adj_list)
    
    if len(curr_route) == L:
        routes.append(curr_route)
    
    
    curr_route = curr_route[:-1]
    return all_routes(L,src,stacks,curr_route,routes,adj_list)
    
    

adj_list={1:[2,6,7],2:[3,4],3:[5],4:[],5:[],6:[8],7:[9,10],8:[],9:[],10:[]}
stacks = []
routes = []

for k in adj_list.keys():
    stack = deque(adj_list[k])
    stacks.append(stack)
    routes = all_routes(3,src=k,stacks=stacks,curr_route=[k],routes=routes,adj_list=adj_list)
    print(routes)





