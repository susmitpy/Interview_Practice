#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:41:58 2020

@author: susmit
"""

past = "past"
to = "to"
quarter = "quarter"
half = "half"
minute = "minute"
minutes = "minutes"
oclock = "o' clock"
words = ["one","two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty"]
tw = {i:j for i,j in zip(list(range(1,21)) + [30],words)}
for i in range(1,10):
    a = str(i)
    b = tw[int(a)]
    tw[int("2"+a)] = "twenty " + b
    tw[int("3"+a)] = "thirty " + b
    tw[int("4"+a)] = "forty " + b
    tw[int("5"+a)] = "fifty " + b

ans = ""
s = " "

h = 5
m = 0

def time_in_words(h,m):
    ans = ""
    if m == 0:
        ans = tw[h] + s + oclock
        return ans
    
    elif m == 30: 
        ans = half + s + past + s + tw[h]
        return ans
        
    elif m < 30:
        if m == 15:
            ans = quarter + s + past + s + tw[h]
            return ans
        
        else:
            ans = tw[m] + s
            if m == 1:
                ans += minute + s
            else:
                ans += minutes + s
            ans += past + s + tw[h]
            return ans
    else:
        if m == 45:
            ans = quarter + s + to + s
         
        else:
            m1 = 60 - m
            ans = tw[m1] + s
            if m1 == 1:
                ans += minute + s
            else:
                ans += minutes + s
            ans += to + s
         
        if h == 12:
            ans += tw[1]
        else:
            ans += tw[h+1]
        
        return ans
        
        
   
        

