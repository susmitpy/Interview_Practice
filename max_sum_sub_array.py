#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:33:19 2019

@author: susmitvengurlekar
"""
"""
0 1 2 3 4 5
4 8 2 7 2 6


"""

def max_sum_sub_array(a,k):
    
    current_running_sum = 0
    max_sum = float("-inf")
    
    for i,j in enumerate(a):
        current_running_sum += j
        if (i >= k-1):
            max_sum = max(max_sum,current_running_sum)
            current_running_sum -= a[i-k-1]
    return max_sum


arr = [4,8,-1,7,2,6]

print(max_sum_sub_array(arr,3))