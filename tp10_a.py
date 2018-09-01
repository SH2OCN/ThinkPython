# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 19:40:46 2018
tp chapter 10
@author: lenovo
"""
def nested_sum(l):
    ans = 0
    for item in l:
        ans += sum(item)
    return ans

def capitalize_all(l):
    res = []
    for i in l:
        res.append(i.capitalize())
    return res

def capitalize_nested(l):
    ans = []
    for item in l:
        ans.append(capitalize_all(item))
    return ans

def only_upper(l):
    ans = []
    for i in l:
        if i.isupper():
            ans.append(i)
    return ans
    
def fun10_3(l):
    ans = []
    count = 0
    for s in l:
        count += s
        ans.append(count)
    return ans
        



