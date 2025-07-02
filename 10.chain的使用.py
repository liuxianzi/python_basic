# -*- coding: utf-8 -*-
"""
 @Time           2025/7/2 17:28
 @File           10.chain的使用.py
 @Description    
 @Author         
"""
import itertools

a = [1, 2]
b = [2, 6]

for num in itertools.chain(a, b):
    print(num)
