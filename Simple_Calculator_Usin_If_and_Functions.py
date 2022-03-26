# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:43:19 2022

@author: Arin
"""

#Simple calculator using if and functions


a=int(input("Enter the first value : "))
b=int(input("Enter the second value : "))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("Select Operation : ")
print(" 1- Add ")
print(" 2- Subtract")
print(" 3- Multiply")
print(" 4- Divide")

op=int(input("Enter what operation you want to perform between 1 to 4 : "))

if op== 1:
    print(add(a,b))
    
elif op==2:
    print(subtract(a,b))
    
elif op==3:
    print(multiply(a,b))
    
elif op==4:
    print(divide(a,b))
    
else:
    print("Invalid Input")