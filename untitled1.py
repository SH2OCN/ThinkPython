# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:33:43 2018
待补充
@author: lenovo
"""

import bisect
t = [0,1,2,3,4]
x = 1.0
print(bisect.bisect_right(t,x))
bisect.insort_left(t,x)
print(t)
bisect.