# -*- coding: utf-8 -*-
"""
 @Time           2025/6/27 19:19
 @File           2.数据库连接池.py
 @Description    
 @Author         
"""
import pymysql
from dbutils.pooled_db import PooledDB
from threading import Thread

# 构建连接池
Pool = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的链接，0表示不创建
    blocking=True,   # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    ping=0,  # ping MySQL服务端，检查是否服务可用。如：0 = None = never, 1 = default = whenever it is requested,
    # 2 = when a cursor is created, 4 = when a query is executed, 7 = always

    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='newdjango',
    charset='utf8'
)

# 利用线程来测试，可以看出是6个 6个...连接一起来的


def task(num):
    # 获取连接
    conn = Pool.connection()
    #
    cursor = conn.cursor()
    # cursor.execute('select * from student')  # 这个查询语句太简单了，看不出效果
    cursor.execute('select sleep(3)')  # 可以看出是6个 6个线程一起运行的
    result = cursor.fetchall()

    cursor.close()
    # 不是销毁这个连接，而是用完了这个连接，将其放回连接池，给其它线程使用
    conn.close()
    print(num, '-------------->', result)


if __name__ == '__main__':
    for i in range(60):
        t = Thread(target=task, args=(i+1,))
        t.start()
