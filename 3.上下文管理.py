# -*- coding: utf-8 -*-
"""
 @Time           2025/6/27 21:24
 @File           3.上下文管理.py
 @Description    
 @Author         
"""


class Base:
    def __enter__(self):
        return '123'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('程序要结束了')


with Base() as obj:
    print(obj)


"""
使用with as 上下文管理，必须定义__enter__和__exit__方法，否则报错，
__enter__的返回值就是as后变量的值
with as 执行结束后会执行 __exit__方法
"""


"""在有些项目可能会见到以下类似代码"""


class F1(object):
    def do_something(self):
        print('do_some thing')


class Context(object):
    def __enter__(self):
        return F1()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with Context() as ctx:
    ctx.do_something()
