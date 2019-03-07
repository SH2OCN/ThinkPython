# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:09:09 2018
批量重命名一个文件夹内的文件。 把没有扩展名的文件加上扩展名".jpg"
@author: lenovo
"""

import os

path = 'D:\\testpic\\' #想要修改的文件所在文件夹的绝对路径

for file in os.listdir(path):

    if os.path.isfile(os.path.join(path,file))==True:

        if file.find('.')<0:

            newname=file+'haha.jpg' #把所有没有扩展名的文件名字后面加上“haha.jpg"

            os.rename(os.path.join(path,file),os.path.join(path,newname))

            print(file,'ok')
            
#        print file.split('.')[-1]