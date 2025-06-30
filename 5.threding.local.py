# -*- coding: utf-8 -*-
"""
 @Time           2025/6/29 18:10
 @File           9.知识点：threding.local.py
 @Description    
 @Author         
"""
import time
import threading


class Foo:
    def __init__(self):
        self.num = 0


obj = Foo()


def task(num):
    obj.num = num
    time.sleep(1)
    print(obj.num)


for i in range(4):
    t = threading.Thread(target=task, args=(i+1, ))
    t.start()


"""
原来的：4个线程 来了，会修改对象的num值，但是因为obj是同一个对象，所以obj.num值会以最后一次修改后的值为准
threding.local: 会为每个线程开辟一块新内存，保证每个线程执行的结果 是它自己的
原来的怎么改造呢：让Foo继承threding.local即可达到目的
"""

obj2 = threading.local()


def task(num):
    obj2.num = num
    time.sleep(1)
    print(obj2.num)


for i in range(4):
    t = threading.Thread(target=task, args=(i+1, ))
    t.start()
