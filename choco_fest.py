#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:39:32 2020

@author: susmit
"""
from time import sleep
n,c,m = 10,2,5
"""
3 3 0 2
1 4 1 2
1 5 1 2




"""


def replace(additional_wrappers,total_chocos,rem,m):
    dm = divmod(additional_wrappers+rem,m) 
    if dm[0] == 0:
        return total_chocos
    total_chocos += dm[0]
    additional_wrappers = dm[0]
    rem = dm[1]
 
    if additional_wrappers+rem < m:
        return total_chocos
    
    return replace(additional_wrappers,total_chocos,rem,m)


rem = 0
stop = False
chocos = n // c
chocos = replace(chocos,chocos,0,m)
print(chocos)