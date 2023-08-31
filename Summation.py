# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 06:45:32 2022

@author: Subhamoy
"""



n = input("Enter Number to calculate sum ")
n = int (n)
sum = 0


# =============================================================================
# # Showing the sequence of numbers
# =============================================================================
# x = range(n+1)
# for n in x:
#     print(n)
# =============================================================================
# =============================================================================

# Calculating the summation of first n numbers
for num in range(0, n+1, 1):
    sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )

