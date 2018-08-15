# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:49:54 2018
把一个整数的个十百千...位存入list中
@author: lenovo
"""

a = 54321
ans = []
l = len(str(a))
for i in range(l):
    k = (a//10**i%10)
    ans.append(k)

print(ans)    

