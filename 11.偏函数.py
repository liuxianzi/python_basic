# -*- coding: utf-8 -*-
"""
 @Time           2025/7/2 17:39
 @File           11.偏函数.py
 @Description    
 @Author         
"""
import functools


def func(a, b):
    print(a)
    print(b)


new_func = functools.partial(func, '你好')
new_func(2)
