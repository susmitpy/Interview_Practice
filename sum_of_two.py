"""
Given two lists: a,b
integer: v
develop a function that takes a,b,v and
returns true if there exists atleast one number 
in a say "a1" and one number in b say "b1" such that
a1 + b1 = v
else return false

Extreme Programming Technique is used.
Tests are written in sum_of_two_test.py before optimising code
to ensure things go smoothly
"""

def sumOfTwo(a,b,v):
    for i in a:
        for j in b:
            if i+j == v:
                return True
    return False
