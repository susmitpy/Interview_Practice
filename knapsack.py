#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:38:45 2019

@author: susmitvengurlekar
"""

weights = [10,20,30]
values  = [60,100,120]
W = 50

def knapsack(weights,values,W):
    total = 0
    d = dict(zip(values,weights))
    elems = sorted(d.items(),reverse=True)
    print(elems)
    for v,w in elems:
        if w <= W:
            total += v
            W -= w
        elif W == 0:
            break
    return total

print(f"Solution 1: {knapsack(weights,values,W)}")
            
    
    
