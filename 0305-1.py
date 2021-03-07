# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:40:38 2021

@author: User
"""
#1-49號隨機選號(不重複)
import random

number=list()
for a in range(6):
    num=random.randint(1,49)
    number.append(num)
    if number.count(num)>1:
        continue
print(number)


    