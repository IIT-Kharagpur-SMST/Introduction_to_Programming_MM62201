# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 06:23:30 2022

@author: Subhamoy
"""

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
            nums = nums + (t[0],) 
    if t[1] not in words: 
            words = words + (t[1],)
            min_n = min(nums)
            max_n = max(nums)
            unique_words = len(words)
            return (min_n, max_n, unique_words)