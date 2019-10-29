#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:22:47 2019

@author: susmitvengurlekar
"""
import numpy as np

s1 = "cart"
s2 = "march"

def edit_distance_numpy(s1,s2):
    n1 = len(s1)
    n2 = len(s2)
    ed = np.zeros((n1+1,n2+1),dtype=int)
    ed[0,:] = list(range(n2+1))
    ed[:,0] = list(range(n1+1))
    for r in range(n1):
        for c in range(n2):
            if s1[r] == s2[c]:
                ed[r+1,c+1] = ed[r,c]
            else:
                ed[r+1,c+1] = min(ed[r,c],ed[r+1,c],ed[r,c+1]) + 1
    return ed[n1,n2]
