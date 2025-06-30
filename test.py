# -*- coding: utf-8 -*-
"""
 @Time           2025/6/28 10:32
 @File           test.py
 @Description    
 @Author         
"""
from tools.sqlhelper import db
from threading import Thread


def task(num):
    sql = 'select sleep(3)'

    with db as cur:
        cur.execute(sql)

    print(num)


if __name__ == '__main__':
    for i in range(60):
        t = Thread(target=task, args=(i+1,))
        t.start()
