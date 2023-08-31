# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:16:19 2023

@author: Mandal
"""

s = "abcdefghijrtzudr"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")
        print(index)