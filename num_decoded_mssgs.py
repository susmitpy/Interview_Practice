#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:08:32 2019

@author: susmitvengurlekar
"""

from string import ascii_lowercase

encoding = {i:j for i,j in zip(ascii_lowercase,list(range(1,27)))}
#print(f"Encoding: {encoding}")

decoding = {j:i for i,j in encoding.items()}
#print(f"Decoding: {decoding}")

def encoder(s):
    return "".join([str(encoding.get(i)) for i in s])

possible_messages = []
combinations = []

def split(s):
    l = len(s)
    if l == 1:
        alpha = decoding.get(int(s))
        if alpha:
            return alpha
        
    
    global combinations
    
    alpha = decoding.get(int(s))
    if alpha:
        combinations.append(alpha)
    
    st = 0
    e = l-1
    m = (st+e)//2
    
    left = split(s[:m+1])
    right = split(s[m+1:])
    
    if l > 2:
        middle = split(s[m:m+2])
        if middle:
            combinations.append(left+middle+right)
    if left and right:
        combinations.append(left+right)
    elif left:
        combinations.append(left)
    elif right:
        combinations.append(right)
    

def decoder(n):
    alpha = split(n)
    if alpha:
        combinations.append(alpha)
    print(combinations)
    return combinations

def main():
    words = ["ab","l","py","ba","abc","abba","sus","susm"]
    for word in words:
        if word in decoder(encoder(word)):
            print("Working: ", word, " ", encoder(word))
        else:
            print("Not Working: ",word, " ", encoder(word))

if __name__ == "__main__":
    main()