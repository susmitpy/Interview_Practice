#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:08:41 2019

@author: susmitvengurlekar
"""

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def check_conditions(node):
    if node.left.left == None:
        if node.left.right == None:
            if (node.left.data < node.data) and (node.right.data > node.data):
                return True
            return False
        else:
            return check_conditions(node.left)
    elif node.left.right == None:
        return check_conditions(node.left)
    
    elif node.right.left == None:
        if node.right.right == None:
            if (node.right.data > node.data):
                return True
            return False
        else:
            check_conditions(node.right)
    
    elif node.right.right == None:
        return check_conditions(node.right)
    
    
    lst = check_conditions(node.left)
    rst = check_conditions(node.right)
    
    return (lst and rst)

def check_binary_search_tree_(root):
    return check_conditions(root)