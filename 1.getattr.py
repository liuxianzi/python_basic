# -*- coding: utf-8 -*-
"""
 @Time           2025/6/1 22:36
 @File           1.getattr.py
 @Description    类的getattr方法
 @Author         
"""


class Goods:

    def get_goods(self):
        print('get_goods被执行了')

    def post_goods(self):
        print('post_goods被执行了')

    def not_found(self):
        print('没有找到要执行的方法')


if __name__ == '__main__':
    goods = Goods()

    # getattr(obj:类对象，name:要调用的类方法名，default:如果没有这个类方法默认执行的类方法)
    handler = getattr(goods, 'post_goods')
    handler()

    handler = getattr(goods, 'put_goods', goods.not_found)
    handler()

