# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 07:53:43 2022

@author: Subhamoy
"""

def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

# Driver Code
num= 12
if num <=0:
    print("Please enter a Positive Number")
else:
        print("Recursion Example: The Fibonacci series for first", num, "numbers is-- ", end=" ")
for i in range(num):
        print(fibonacciSeries(i), end=" ")


