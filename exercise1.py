# -*- coding: utf-8 -*-

t = [[0 for j in range(3)] for i in range(3)]
print(t)
t[0][1]=2
print(t)
print('-------'*8)


import numpy
c = numpy.zeros((3,3),int)
print(c)
c[0][1] = 2
print(c)
print('-------'*8)

#a = [[0]*3]*3
a = [[0,0,0] for i in range(4)]
print(a)
a[0][1]=2
print(a)