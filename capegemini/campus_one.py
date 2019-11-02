#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:43:36 2019

@author: susmitvengurlekar
"""
from collections import defaultdict

def next_station(L,CA,curr_route):
    if len(curr_route) == L:
        return curr_route
    if curr_route[0] == -1:
        return [-1]
    from_s = curr_route[-1]
    ns_found = False
    for nsp in CA[from_s]:
        if nsp not in curr_route:
            curr_route.append(nsp)
            ns_found=True
            break
    if ns_found:
        return next_station(L,CA,curr_route)
    return [-1]

def main():
# =============================================================================
#     L = int(input())
#     N = int(input())
#     R = int(input())
#     C = int(input())
# =============================================================================
    L=7
    N=9
    R=9
    C=2
# =============================================================================
#     CA = defaultdict(list)
#     for r in range(R):
#         t = [int(n) for n in input().split(" ")]
#         if t[1] not in CA[t[0]]:
#             CA[t[0]].append(t[1])
#         if t[0] not in CA[t[1]]:
#             CA[t[1]].append(t[0])
# =============================================================================
    CA={1: [4, 5, 7], 4: [1, 3, 6], 5: [1, 6], 7: [1, 6], 6: [5, 2, 4, 7], 2: [3, 6], 3: [2, 4]}
    print(CA)
    for i, j in CA.items():
        for nsp in j:
            r = [i,nsp]
            r = next_station(L,CA,r)
            print(r)
    
main()
"""
7

9

9

2

1 4

5 1

1 7

5 6

2 3

3 4

2 6

4 6

6 7

"""