# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 02:49:50 2022

@author: Subhamoy
"""

# import random
# choices = list(range(14))
# random.shuffle(choices)
# print(choices.pop())
# while choices:
#     if input('Want another random number?(Y/N)' ).lower() == 'n':
#         break
#     print(choices.pop())
    
    
    
import random

print("Create a sampled list of random integers without duplicates")
sampled_op = random.sample(range(9), 5)
print(sampled_op)