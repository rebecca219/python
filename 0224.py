# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:44:57 2021

@author: USER
"""
"""
1.輸入迴圈次數，判斷哪些數值是奇數，哪些是偶數?
2.呈上題，輸入迴圈次數，計算數值中為偶數之加總，
最後印出加總值。
"""
number=int(input("請輸入任意數字:"))
y=0
for x in range(1,number+1):
    if x % 2 == 0:
        print(x,"為偶數")
        y+=x
        
    else:
        print(x,"為奇數")

print("total=",y)