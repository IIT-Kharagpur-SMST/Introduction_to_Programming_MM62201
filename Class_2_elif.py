# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:12:23 2023

@author: Mandal
"""
## Write code to check the validity of a person to vote

age = int(input("Enter your age: ")) # take the age as an integer input
if age >= 18: # check if the age is greater than or equal to 18
    print("You are eligible to vote.") # print a message if true
elif age < 0: # check if the age is less than 0
    print("Invalid age.") # print a message if true
else: # otherwise
    print("You are not eligible to vote.") # print a message if false
