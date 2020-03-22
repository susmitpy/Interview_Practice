#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:53:06 2020

@author: susmitvengurlekar
"""

from collections import Counter

s = "spo"
n = len(s)
fd = Counter(s)
res = []

while n > 0:
    fd = dict(sorted(fd.items(),key=lambda x: x[0]))
    for k, v in fd.items():
        if v != 0:
            res.append(k)
            fd[k] -= 1
            n -= 1
    fd = dict(sorted(fd.items(),key=lambda x: x[0],reverse=True))
    for k, v in fd.items():
        if v != 0:
            res.append(k)
            fd[k] -= 1
            n -= 1

print("".join(res))

    