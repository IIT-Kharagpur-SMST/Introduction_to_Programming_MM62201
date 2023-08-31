# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#define a function
y =55;
print (y)

def func1():
   print ("I am learning Python function")
   print ("still in func1")
   y =59;
   print (y)

func1()

print(y)

def square(x):
   	return x*x
print(square(4))

def multiply(x,y=0):
 	print("value of x=",x)
 	print("value of y=",y)
    
 	return x*y
  
print(multiply(y=2,x=4))