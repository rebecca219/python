# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:57:40 2021

@author: User
"""
"""
用for迴圈印出
123456789
12345678
1234567
123456
12345
1234
123
12
1
"""

for a in range(9,0,-1):
    for i in range(1,a+1):
        print(i,end='')
    print()