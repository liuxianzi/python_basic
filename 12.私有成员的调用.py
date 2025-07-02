# -*- coding: utf-8 -*-
"""
 @Time           2025/7/2 17:44
 @File           12.私有成员的调用.py
 @Description    
 @Author         
"""


class Foo:
    def __init__(self):
        self.name = 'xiaoa'
        self.__age = 123


obj = Foo()

print(obj.name)
# print(obj.__age)  # 访问私有成员会报错
# 对象._函数名__私有属性：强行获取
print(obj._Foo__age)  # 强制获取私有成员
