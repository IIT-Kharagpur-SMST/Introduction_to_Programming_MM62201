# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 01:20:30 2022

@author: Subhamoy
"""

from random import *
import sys
sys.tracebacklimit=0

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
i= len(items);

#x = sample(items,  1)   # Pick a random item from the list
#print(x[0])

for i in range(14):
   if i >= 3:
       items1 = sample(items, 3)    # Pick 4 random items from the list
       print(items1)
       items= [elt for elt in items if elt not in items1]
       i= len(items); 
       print(items)
       

   