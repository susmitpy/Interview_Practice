#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:32:56 2020

@author: susmitvengurlekar
"""
"""
def process(filename):
    f = open(filename,"r")
    f.close()
    

   
    f = open(filename[:-3]+"_ans.txt","w")
    f.close()
    
filenames = ["a_example.txt"]#,"b_small.in","c_medium.in","d_quite_big.in","e_also_big.in"]

for f in filenames:
    process(f)

"""
from math import ceil



f = open("b_read_on.txt","r")
#Sign Up, Shipping Rate, BookS
libs = {} # {0: {n:5,su:2,sr:2,bs:[0,1,2,3,4]}}
B,L,S = [int(i) for i in f.readline().split(" ")]
scores = {i:j for i,j in zip(range(0,B),[int(i) for i in f.readline().split(" ")])}
highest_score_first_scores = dict(sorted(scores.items(),key=lambda x: x[1],reverse=True))
#scores = [int(i) for i in f.readline().split(" ")]

for i in range(L):
    libs[i] = {}
    data = [int(i) for i in f.readline().split(" ")]
    libs[i]["n"] = data[0]
    libs[i]["su"] = data[1]
    libs[i]["sr"] = data[2]
    libs[i]["bs"] = [int(i) for i in f.readline().split(" ")]

f.close()
#print(B,L,S)
#print(scores)
#print(libs)

libs_sign_up_order =[]

sorted_by_sign_up = dict(sorted(libs.items(),key=lambda x: x[1]["su"]))
days_rem = S
for k, v in sorted_by_sign_up.items():
    if (days_rem - v["su"] < 0):
        break
    days_rem -= v["su"]
    libs_sign_up_order.append(k)
    
books_l_scan = []

days_rem = S - libs[libs_sign_up_order[0]]["su"]
for l in libs_sign_up_order:
   # print("Lib: " + str(l))
    days_required = ceil(libs[l]["n"]/libs[l]["sr"])
    #print(f"Days required: {days_required}")
    if (days_required > days_rem):
        days_required = days_rem
        
    days_rem -= days_required
    books_scanned_n = min(days_required*libs[l]["sr"],libs[l]["n"])
    books_scanned_scores = {i:scores[i] for i in libs[l]["bs"]}
    mapped = sorted(books_scanned_scores.items(),key=lambda x: x[1],reverse=True)
    ss = [mapped[i][0] for i in range(books_scanned_n-1)]
    books_l_scan.append(ss)
    #books_l_scan.append([i[0] for i ])
    
f = open("b_ans.txt","w")   
    
#print("Output")
f.write(str(len(libs_sign_up_order)) + "\n")
for i in range(len(libs_sign_up_order)):
    f.write(str(libs_sign_up_order[i]) + " " + str(len(books_l_scan[i]))+"\n")
    f.write(" ".join([str (i) for i in books_l_scan[i]]))
    
f.close()

    
        
