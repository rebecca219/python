# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:11:03 2021

@author: User
"""
'''
終極密碼
猜範圍數字
'''
import random
ans=random.randint(1,100)
count=0
lowest=1
highest=100
guess=0
while ans!=guess:
    guess = int(input("輸入"+str(lowest)+'-'+str(highest)+'的數:')) 
    if guess < ans:
        lowest = guess+1
    else:
        highest = guess-1
    count+=1
print("Bingo!共猜:",count,"回")
