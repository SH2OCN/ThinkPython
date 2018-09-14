# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Sun Sep 02 19:47:50 2018

@author: lenovo
"""

#11-1
from tp10_b import word_list1
def make_dict():
    t = word_list1()
    mydict  = dict()
    for i in range(len(t)):
        mydict[t[i]] = i
    return mydict
    
'''
#三种方法的耗时对比：
from tp10_b import my_bisect
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
    '''统计string里每个字母出现的次数'''
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
    '''反转字典'''
    ans = dict()
    for k,v in d.items():
        print(k,v)
        ans.setdefault(v,[]).append(k)
        
    return ans
#11-6
k = {0:0,1:1}
def fibonacci(n):
    global k
    if n in k:
        return k[n]
    else:
        ans = fibonacci(n-1) + fibonacci(n-2)
        k[n] = ans
        return ans    
#11-7
memo = dict()
def ack(m,n):
    global memo
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 0:
        ans = n+1
        memo[(m,n)] = ans
        return ans
    elif m>0 and n==0:
        ans = ack(m-1,1)
        memo[(m,n)] = ans
        return ans
    elif m>0 and n>0:
        ans = ack(m-1,ack(m,n-1))
        memo[(m,n)] = ans
        return ans
#11-9
def has_duplicates(l):
    d = dict()
    for i in l:
        if i in d:
            return True
        else:
            d[i] = 1
    return False

#11-10        
def rotate_letter(l,n):
    return chr((ord(l)-ord('a')+n)%26+ord('a'))

def rotate_word(w,n):
    ans = ''
    for l in w:
        ans = ans + rotate_letter(l,n)
    return ans

def rot_to_a(w):
    '''把word移到以a开头'''
    return rotate_word(w,ord('a')-ord(w[0]))


def rotate_pairs(t):
    d = dict()
    for w in t:
        rot = rot_to_a(w)
        d.setdefault(rot,[]).append(w)
    for v in d.values():
        if len(v) > 1:
            print(v)
'''
t = word_list1()            
d = rotate_pairs(t)
'''








