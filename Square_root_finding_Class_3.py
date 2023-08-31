# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:05:36 2023

@author: Mandal
"""

## Using in-build math function
print("Enter a Number: ")
num = int(input())
squareroot = num ** 0.5
print("\nSquare Root =", squareroot)

## Using inbuild Math Library function 
import math

# Input the number
num = float(input("Enter a number: "))

# Calculate the square root
sqrt = math.sqrt(num)

# Print the result
print(f"The square root of {num} is {sqrt}")
