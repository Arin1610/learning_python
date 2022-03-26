# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:13:06 2022

@author: Arin
"""
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division ")
x=int(input("Enter First Number : "))
y=int(input("Enter Secound Number : "))
op=int(input("Enter what operation you want to perform between 1 to 4 : "))

if op== 1:
    print("Your Answer is " , x+y)
elif op==2:
    print("your Answer is " , x-y)
elif op==3:
    print("Your Answer is " , x*y)
elif op==4:
    print("Your Answer is " , x/y)
else:
    print("Invalid")
    