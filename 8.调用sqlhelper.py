# -*- coding: utf-8 -*-
"""
 @Time           2025/6/30 22:18
 @File           8.调用sqlhelper.py
 @Description    sqlhelper2的使用
 @Author         
"""
# sqlhelper2的使用
from tools.sqlhelper2 import db

with db as c1:  # 同一个对象，两个线程，内部利用线程local隔离的
    c1.fetchone('xxx')
    with db as c2:
        c2.fetchone('xxx')


with db as cursor:
    cursor.fetchone('xxx')


# sqlhelper3的使用
from tools.sqlhelper3 import SqlHelper


with SqlHelper() as cursor1:  # 两个对象 内存隔离的
    cursor1.fetchone('xxx')
    with SqlHelper() as cursor2:
        cursor2.fetchone('xxx')

with SqlHelper() as cursor3:
    cursor3.fetchone('xxx')

# 如果不明白 去看该文件夹下的关于threading.local的3个py文件
