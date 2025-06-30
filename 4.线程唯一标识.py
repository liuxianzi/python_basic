# -*- coding: utf-8 -*-
"""
 @Time           2025/6/30 18:50
 @File           4.线程唯一标识.py
 @Description    
 @Author         
"""
import time
import threading
from threading import get_ident


def task():
    # get_ident 是 threading 模块中的一个函数，用来获取当前线程的“线程标识符”（线程ID）
    ident = get_ident()
    # time.sleep(1)
    print(ident)  # ident重复 是因为线程结束后，ID被操作系统回收并分配给新线程。


for i in range(20):
    t = threading.Thread(target=task)
    t.start()
