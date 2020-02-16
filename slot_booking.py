#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:37:49 2020

@author: susmitvengurlekar
"""

"""
2 persons: p1, p2
Meeting timings of each person: m1 [[start_time,end_time],[]...], m2 [[],[]....]
time bounds of each person:  b1 [min_time,max_time], b2 [min_time,max_time]
duration: d
time in 24 hr format

Sample input
m1: [["9:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
b1: ["9:00","20:00"]

m2: [["10:00","11:30"],["12:30","14:30"],["14:30","15:00"],["16:00","17:00"]]
b2: ["10:00","18:30"]

30

sample output:
[["11:30","12:00"],["15:00","16:00"],["18:00","18:30"]]

f1,f2: free time slots duration >= 30 of p1, p2

"""

m1 = [["9:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
b1 = ["9:00","20:00"]
m2 = [["10:00","11:30"],["12:30","14:30"],["14:30","15:00"],["16:00","17:00"]]
b2 = ["10:00","18:30"]
d = 30

def convert_to_int(time):
    return int(time.replace(":",""))

def get_free_time_slots(m,b,d):
    """
    Returns free time slots of duration >= d
    within limits of b
    """
    f = []
    # Starting free slot
    m1s = convert_to_int(m[0][0])
    bs = convert_to_int(b[0])
    
    if (m1s - bs) >= d:
        f.append([b[0],m[0][0]])
        
    # Between free slots
    n = len(m) # No of meetings
    for i in range(n-1):
        mae = convert_to_int(m[i][1])
        mbs = convert_to_int(m[i+1][0])
        
        if (mbs - mae >= 30):
            f.append([m[i][1],m[i+1][0]])


    # Ending free slot
    mne = convert_to_int(m[-1][1])
    be = convert_to_int(b[1])
    
    if (be - mne) >= d:
        f.append([m[-1][1],b[1]])
    
    return f

def get_common_free_slots(f1,f2,d):
    """ 
    Returns common free slots from f1, f2
    with duration >= d
    """
    cf = []
    return cf

f1 = get_free_time_slots(m1,b1,d)
f2 = get_free_time_slots(m2,b2,d)

print("Free time slots:")
print(f"P1: {f1}")
print(f"P2: {f2}")

cf = get_common_free_slots(f1,f2,d)
