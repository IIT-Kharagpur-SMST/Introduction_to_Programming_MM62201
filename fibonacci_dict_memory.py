# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:31:35 2023

@author: Mandal
"""

#####################################
# EXAMPLE:  fibonacci
#####################################

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2}

argToUse = 34
#print("")
#print('using fib')
#print(fib(argToUse))
#print("")
#print('using fib_efficient')
print(fib_efficient(argToUse, d))