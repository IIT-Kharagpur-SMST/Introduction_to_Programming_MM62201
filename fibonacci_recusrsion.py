# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 07:53:43 2022

@author: Subhamoy
"""
import time
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

# Driver Code
num= 40

tic= time.perf_counter()
if num <=0:
    print("Please enter a Positive Number")
else:
        print("Recursion Example: The Fibonacci series for first", num, "numbers is-- ", end=" ")
for i in range(num):
        print(fibonacciSeries(i), end=" ")
toc= time.perf_counter()
print(f"The time is {toc - tic:0.4f} seconds")
