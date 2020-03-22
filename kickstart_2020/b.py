#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:39:20 2020

@author: susmitvengurlekar
"""
import numpy as np
"""
t = int(input())
for tc in range(t):
    N,K,P = [int(i) for i in input().split(" ")]
    stacks= []
    for i in range(N):
        stacks.append([int(i) for i in input().split(" ")])
    to = 0
    rem = P
    while rem > 0:
        sums = [sum(i[:rem]) for i in stacks]
        max_indice = np.argmax(sums)
        to += stacks[max_indice][0]
        rem -= 1
        stacks[max_indice].pop(0)
     
    
    print("Case #" +  str(tc+1) + ": " + str(to))
  """ 

"""
80
80


3      2     1
160    80    0
65     65    15
30     30    20


"""

N,K,P = 3,3,5
stacks= [[120,1,2],[4,240,360],[5,1,2]]
to = 0
rem = P
while rem > 0:
    sums = [sum(i[:rem]) for i in stacks]
    max_indice = np.argmax(sums)
    to += stacks[max_indice][0]
    rem -= 1
    stacks[max_indice].pop(0)
 

print("Case #" +  str(1) + ": " + str(to))

    
        