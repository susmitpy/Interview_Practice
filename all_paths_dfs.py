#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:41:43 2019

@author: susmitvengurlekar
"""

from collections import deque
adj_list={1:[2,3],2:[4,5],3:[6,7],4:[],5:[],6:[],7:[]}

stack = deque()
routes = []

def push_children(adj_list, stack, routes,curr_route,links_remaining):
    if links_remaining != 0:
        curr_route.append(stack.pop())
 
    print(f"Curr route: {curr_route}")
    print(f"Links remaining: {links_remaining}")
    print("Routes: ",routes)
    if len(adj_list[curr_route[-1]]) != 0:
        for next_node in adj_list[curr_route[-1]]:
            stack.append(next_node)
        print(f"Stack: {stack}")
        return push_children(adj_list,stack,routes,curr_route,links_remaining)
    routes.append(curr_route)
    print("Stack: ",stack)
    if len(stack) == 1:
        return push_children(adj_list,stack,routes,[curr_route[0]],links_remaining-1)
    return push_children(adj_list,stack,routes,curr_route[:-1],1)
    

for src in adj_list.keys():
    stack.append(src)
    routes = push_children(adj_list,stack,routes,[],len(adj_list[src]))
    print(f"Routes: {routes}")
    break
    
