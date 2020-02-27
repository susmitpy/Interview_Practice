#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:32:39 2020

@author: susmitvengurlekar
"""

def process(filename):
    f = open(filename,"r")
    f.close()


   
    f = open(filename[:-3]+"_ans.txt","w")
    f.close()
    
filenames = ["a_example.in","b_small.in","c_medium.in","d_quite_big.in","e_also_big.in"]

for f in filenames:
    process(f)


