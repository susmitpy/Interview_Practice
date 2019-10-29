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



def decoder(n):
    poss_mssgs = []
    l = len(n)
    for i in range(n):
        pass
    
    return poss_mssgs

def main():
    words = ["ab","l","py","abc"]
    for word in words:
        if word in decoder(encoder(word)):
            print("Working: ", word, " ", encoder(word))
        else:
            print("Not Working: ",word, " ", encoder(word))

if __name__ == "__main__":
    main()