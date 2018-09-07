# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Sun Sep 02 19:47:50 2018

@author: lenovo
"""

#11-1
def make_dict():
    t = word_list1()
    mydict  = dict()
    for i in range(len(t)):
        mydict[t[i]] = i
    return mydict
    
'''
#三种方法的耗时对比：
from tp10_b import word_list1, my_bisect
import time
t = word_list1()
mydict = make_dict()

t1 = time.clock()
print 'prairie' in mydict #字典方法
t2 = time.clock()
print 'prairie' in t      #列表方法
t3 = time.clock()
print my_bisect(t,'prairie') #二分方法
t4 = time.clock()

print t2 - t1
print t3 - t2
print t4 - t3
'''

#11-2
def histogram(string):
    ans = dict()
    for letter in string:
        ans[letter] = ans.get(letter,0) + 1 #有，则把值加1；没有，则令值为1
    return ans
#11-3
def print_hist(h):
    t = h.keys()
    for k in t:
        print (k,h[k])
    return None  
#11-4
def reverse_lookup(d,v):
    ans = list()
    for k in d:
        if d[k] == v:
            ans.append(k)
    return ans
#11-5
def invert_dict(d):
    ans = dict()
    for k in d:
        if d[k] not in ans:
            ans[d[k]] = [k]
        else:
            ans[d[k]].append(k)
    return ans
    
def invert_dict2(d): #重点看
    ans = dict()
    for k,v in d.items():
        ans.setdefault(v,[]).append(k)
    return ans

    
s = 'bananab'
h = histogram(s)
print (h)
ans = invert_dict2(h)
print (ans)







