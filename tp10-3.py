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
   
#10-8
def has_duplicates(l):
    for i in l:
        if l.count(i) != 1:
            return True
    return False
'''
import random
num = 1000    #一共测试1000次
ans = 0       #记录有相同的次数
for i in range(num):
    birth = [random.randint(1,365) for x in range(23)] #随机生成23个生日
    if has_duplicates(birth):
        ans = ans + 1
p = ans * 1.0 / num  #概率
print p
'''            
#10-9
def remove_duplicates_1(l):
    '''第一种，按原顺序'''
    newlist = []
    for s in l:
        if s not in newlist:
            newlist.append(s)
    return newlist
def remove_duplicates_2(l):
    '''第二种，不按原顺序'''
    return list(set(l))
def remove_duplicates_3(l):
    '''第三种，按原顺序'''
    return sorted(set(l),key = l.index)

#10-10
import time
def word_list1():
    fin = open('words.txt')
    t = []
    for line in fin:
        t.append(line.strip())
    return t
def word_list2():
    fin = open('words.txt')
    t = []
    for line in fin:
        t = t + [line.strip()]
    return t
s = time.clock()
time.sleep(6)
e = time.clock()
print e-s    




