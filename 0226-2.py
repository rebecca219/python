# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:15:01 2021

@author: User
"""
"""
由使用者輸入一個數值，透過for迴圈
從1~數值做加總，並印出總和。
"""

number=int(input("Key in a number:"))
total=0
if number ==0:
   print("total=",total+1)

else:
    for i in range(1,number+1):
        total+=i
    print("total=",total)
    