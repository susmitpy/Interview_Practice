#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:12:09 2020

@author: susmitvengurlekar
"""

is_vowel = lambda x: x in ["a","e","i","o","u"]
s = "eleetminicoworoep"
n = len(s)
ls = []
k = 1

occurence_num = [] # (True,1..n), (False,1..n)
d = dict()
for i in s:
    if i in d:
        occurence_num.append((is_vowel(i),d[i]+1))
        d[i] += 1
    else:
        d[i] = 1
        occurence_num.append((is_vowel(i),1))

