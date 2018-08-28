# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:13:30 2018
Think Python Chapter 10 exercises
@author: lenovo
"""
from collections import Counter
#10-6
def is_sorted(l):
    return l == sorted(l)
    
#10-7
def is_anagram(s,t):    
    return Counter(s)==Counter(t) if len(s)==len(t) else False
    
a = 'aleppp'
b = 'ppael'
print is_anagram(a,b)
