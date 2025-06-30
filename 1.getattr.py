# -*- coding: utf-8 -*-
"""
 @Time           2025/6/1 22:36
 @File           1.getattr.py
 @Description    类的getattr方法
 @Author         
"""


# class Goods(object):
#
#     def get_goods(self):
#         print('get_goods被执行了')
#
#     def post_goods(self):
#         print('post_goods被执行了')
#
#     def not_found(self):
#         print('没有找到要执行的方法')
#
#     def __getattr__(self, item):
#         # 当调用属性不存在时，才会走这里
#         print('调用到这了')
#
#
# goods = Goods()
# goods.text = 'hello'
# print(goods.text)
# goods.s  # 如果获取没有的属性，会去__getattr__方法，这里会执行` print('调用到这了')` 也不会报错
# # getattr(obj:类对象，name:要调用的类方法名，default:如果没有这个类方法默认执行的类方法)
# handler = getattr(goods, 'post_goods')
# handler()
#
# # 如果定义了__getattr__方法，就不会执行默认方法，会走到__getattr__方法里
# handler = getattr(goods, 'put_goods',  goods.not_found)
# handler()


class Foo(object):
    def __init__(self):
        # self.storage = {}
        """
        会报错：RecursionError: maximum recursion depth exceeded，递归错误：超过最大递归深度
        因为init的时候 self.storage = {}会自动调用__setattr__方法，而__setattr__中的赋值操作又会调用__setattr__方法，如此返回，陷入递归

        所以 在init这里，使用父类的默认的__setattr__方法
        """
        super().__setattr__('storage', {})

    def __setattr__(self, key, value):
        self.storage[key] = value

    def __getattr__(self, item):
        return self.storage[item]


obj = Foo()
obj.name = 'xiaoming'  # 给obj设置属性，会调用__setattr__方法，
print(obj.name)  # xiaoming
print(obj.__dict__)  # {'storage': {'name': 'xiaoming'}}
