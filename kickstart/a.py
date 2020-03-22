#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:25:43 2020

@author: susmitvengurlekar
"""



t = int(input())
for tc in range(t):
    N, B = [int(i) for i in input().split(" ")]
    H = [int(i) for i in input().split(" ")[:N]]
    H.sort()
    rem = B
    c = 0
    for i in H:
        if i <= rem:
            rem -= i
            c += 1
        else:
            break
    print("Case #" +  str(tc+1) + ": " + str(c))