# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 08:00:11 2022

@author: Subhamoy
"""

def factorial(n):
    
    res = 1
      
    for i in range(2, n+1):
        res *= i
    return res


def factorial_rec(n):
 
    # single line to find factorial
    if (n==1 or n==0) :
        return 1 
    else:
        return n * factorial_rec(n - 1)


# Driver Code
num = 7;
print("Factorial of", num, "is",
factorial(num))
print ("Factorial of",num,"is",
      factorial_rec(num))
 

