# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:04:26 2023

@author: Mandal
"""
## Printing a value
print ('Hello World')

mystring = 'Hello'
print(mystring)

## Which operations are Legal and what is not-legal (Operator- Oparand model)

n = 5;

5*'ab'
5+'ab'
n*'ab'
n+'ab'


# Data Types and Operations
## Scaler Objects

type(5)
type (5.5)
type(n)
test1 = 3<5
test2 = 5<3
type (3<5)

## Type Conversions
a= float (3.8)
int (a)

##################################

pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)

# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)


#############################
#### COMMENTING LINES #######
#############################
# to comment MANY lines at a time, highlight all of them then CTRL+1
# do CTRL+1 again to uncomment them
# try it on the next few lines below!

#area = pi*(radius**2)
#print(area)
#radius = radius + 1
#area = pi*(radius**2)
#print(area)

#############################
#### AUTOCOMPLETE #######
#############################
# Spyder can autocomplete names for you
# start typing a variable name defined in your program and hit tab 
# before you finish typing -- try it below

# define a variable
a_very_long_variable_name_dont_name_them_this_long_pls = 0

# below, start typing a_ve then hit tab... cool, right!
# use autocomplete to change the value of that variable to 1

input()
