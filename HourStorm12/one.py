#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 21:11:12 2019

@author: susmitvengurlekar
"""
"""
10 20 30 40 50
0, 4, 2
2, 4, 3
3, 4, 3

"""


def bs(s,e):
    print(f"S: {s}\tE: {e}")
    if (s >= e):
        return "NO"      
    m = (s+e) // 2
    if (m == s) and arr[e] == q:
        return "YES"
        
    if arr[m] == q:
        return "YES"
    elif arr[m] < q:
        return bs(m,e)
    return bs(s,m)

N, Q = [int(i) for i in input().split(" ")]
arr = [int(i) for i in input().split(" ")]
arr.sort()

for i in range(Q):
    q = int(input())
    print(bs(0,N-1))







