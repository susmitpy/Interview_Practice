#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:21:25 2020

@author: susmitvengurlekar
"""


t = int(input())
for tc in range(t):

    N,P = [int(i) for i in input().split(" ")]
    S = [int(i) for i in input().split(" ")[:N]]
    S.sort()
    window = None
    last_max = 0
    hours = []
    if P != N:
            
        for i in range(N-P):
            if not window:
                window = S[0:P]
            else:
                window.pop(0)
                window.append(S[i+P])
                
            m = window[-1]
            h = 0
            for i in window:
                h += (m-i)
            hours.append(h)
    else:
        m = S[-1]
        for i in S:
            h += (m-i)
        hours.append(h)
        
        
    ans = min(hours)
    print(f"Case #{tc+1}: {ans}")

    
    
    
        
        
    
    
   
    
