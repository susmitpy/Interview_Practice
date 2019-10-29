#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:05:31 2019

@author: susmitvengurlekar
"""
import random
#from collections import Counter
from itertools import permutations
from string import ascii_lowercase as letters

# =============================================================================
# a_to_d = {i:j for i,j in zip(letters,range(1,27))}
# d_to_a = {j:i for i,j in a_to_d.items()}
# =============================================================================

# =============================================================================
# def next_letter(l):
#     letter_num = a_to_d.get(l)
#     if letter_num == 26:
#         return d_to_a.get(1)
#     print(l)
#     return d_to_a.get(letter_num+1)
# 
# 
# def next_word(word,index_to_be_changed,letters_allowed_counter):
#     unchanged_word_left = word[:index_to_be_changed]
#     if index_to_be_changed == -1:
#         unchanged_word_right = ""
#     else:
#         unchanged_word_right = word[index_to_be_changed+1:]
#     print(f"index to be changed: ",index_to_be_changed)
#     changed_word = unchanged_word_left + next_letter(word[index_to_be_changed]) + unchanged_word_right
#     print("changed word: ",changed_word)
#     c = Counter(letters_allowed_counter)
#     if letters_allowed_counter - c:
#         return changed_word
#     print(f"index to be changed: ",index_to_be_changed)
#     
#     return next_word(changed_word,index_to_be_changed,letters_allowed_counter)
# =============================================================================
    

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    if w == "".join(sorted(list(w),reverse=True)):
        return "no answer"
    
    sorted_perms = sorted(permutations(w))
    unique_find_start = "".join(sorted_perms[sorted_perms.index(tuple(w))+1])
    i = 2

    while unique_find_start == w:
        unique_find_start = "".join(sorted_perms[sorted_perms.index(tuple(w))+i])
        i+=1
    return unique_find_start


f = open("bigger.txt","r")
test = f.readlines()
f.close()

for i, word in enumerate(test):
    if i % 5000 == 0:
        print("Reached: ",i)
    try:
        biggerIsGreater(word.strip())
    except Exception as e:
        print(e)
        

    #a_to_d = {i:j for i,j in zip(letters,range(1,27))}
    #print(a_to_d)
    #d_to_a = {j:i for i,j in a_to_d.items()}
    #print(d_to_a)
# =============================================================================
#     s_num = int("".join([str(a_to_d[i]) for i in w]))
#     print(s_num)
# =============================================================================
    #last = int("".join(sorted(list(str(s_num)),reverse=True)))
# =============================================================================
#     last = int("".join([str(a_to_d.get(i)) for i in sorted(list(w),reverse=True)]))
#     print(last)
#     c = Counter(w)
#     print(c)
#     next_min_word = next_word(w,-1,c)
#     print(next_min_word)
# =============================================================================
# =============================================================================
#     for num in range(s_num+1,last+1):
#         if "0" not in str(num):
#             if num == 48113:
#                 print("Error occurs here, you are splitting by each digit")
#             c1 = Counter("".join([d_to_a.get(int(i)) for i in str(num)]))
#             if not c - c1: 
#                 print(num)
#                 return "".join([d_to_a.get(int(i)) for i in str(num)])
# =============================================================================

# =============================================================================
# def generate_test_words(n):
#     test = []
#     for i in range(n):
#         test.append("".join(random.sample(letters,random.randint(1,15 ))))
#     return test
#         
# 
# test = generate_test_words(100000)      
# for i, word in enumerate(test):
#     if i % 50 == 0:
#         print(i)
#     try:
#         biggerIsGreater(word)
#     except RuntimeError:
#         print(i)
#         print(word)
# =============================================================================
