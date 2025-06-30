# -*- coding: utf-8 -*-
"""
 @Time           2025/6/30 19:57
 @File           6.自定义threading.local.py
 @Description    自定义实现threading.local的功能
 @Author         
"""
import time
import threading


"""
实现以下效果：
storage = {
    1111:{'x1':1},
    1112:{'x1':2}
    1113:{'x1':3}
    1114:{'x1':4}
    1115:{'x1':5}
}
"""


class Foo(object):
    def __init__(self):
        super().__setattr__('storage', {})

    def __setattr__(self, key, value):
        ident = threading.get_ident()
        if ident not in self.storage:
            self.storage[ident] = {key: value}
        else:
            self.storage[ident][key] = value

    def __getattr__(self, item):
        ident = threading.get_ident()
        if ident in self.storage:
            return self.storage[ident].get(item)
        return None


obj = Foo()


def task(num):
    obj.num = num
    time.sleep(1)
    """
    为了模拟复杂些的场景，这个过程太简单了，会在下一个线程来之前迅速返回当前的值，所以加个延时，让它执行的慢些
    # 可以看出 obj.num都等于5（被后边的线程改掉了当前线程的值
    # 为了防止这种现象，利用threading的ident来辨识
    """
    print(obj.num)


for i in range(5):
    t = threading.Thread(target=task, args=(i+1, ))
    t.start()
