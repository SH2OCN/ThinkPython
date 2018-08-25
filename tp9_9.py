# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 16:35:56 2018
cartalk3年龄之谜
@author: lenovo
"""
def is_rev(i,j):
    '''判断两个数i和j是否互为反转
    '''
    return str(i).zfill(2) == str(j).zfill(2)[::-1]

def rev_times(k):
    '''计算在0~100之内‘相差k’能出现的反转次数
    '''
    num = 0
    for i in range(100-k):
        if is_rev(i,i+k):
            num = num + 1
            print i, i+k
    return num
    
print rev_times(18)
    
    
    
    
    
    