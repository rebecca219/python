# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:13:57 2021

@author: User
"""

n=3
k=0
for b in range(1,8,2):
    if b<7:
        n-=1
        print(n*" ",b*"*")
    else:
        print(b*"*")

for c in range(5,0,-2):
    k+=1 
    print(k*" ",c*"*",sep='')