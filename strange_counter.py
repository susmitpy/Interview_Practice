#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 23:47:17 2020

@author: susmitvengurlekar

Hackerrank Problem: Strange Counter
Link: https://www.hackerrank.com/challenges/strange-code/problem
"""

n = int(input())

cycle_start_time = 1
cycle_end_time = 3

cycle_start_value = 3

while True:
    if n <= cycle_end_time and n >= cycle_start_time:
        break
    
    cycle_start_time = cycle_end_time + 1
    cycle_end_time = (cycle_start_value * 4) - 2 - 1
    cycle_start_value = cycle_start_value * 2

ans = cycle_start_value - (n - cycle_start_time)
print(ans)