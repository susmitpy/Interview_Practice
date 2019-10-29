#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:03:07 2019

@author: susmitvengurlekar
"""

from collections import deque

def isBalanced(s):
    stack = deque()

    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]

    for i in s:
        if i in opening:
            stack.append(i)
        else:
            if len(stack) == 0:
                return "NO"
            if not opening.index(stack.pop()) == closing.index(i):
                return "NO" 
    return "YES"


