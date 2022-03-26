# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 00:33:12 2022

@author: Arin
"""

#to print the following image

for i in range(5):
    for a in range(i):
        print(" ", end="")
    for j in range(i, 5):
        print("* ", end="")
    print()
for i in range(5):
    for a in range(-4, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()