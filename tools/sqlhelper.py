# -*- coding: utf-8 -*-
"""
 @Time           2025/6/27 20:31
 @File           sqlhelper.py
 @Description    数据库连接池 比较规范的写法（当做一个公共的工具，被其他文件调用
 @Author         
"""
import pymysql
from dbutils.pooled_db import PooledDB


class SqlHelper(object):
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的链接，0表示不创建
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            ping=0,  # ping MySQL服务端，检查是否服务可用。如：0 = None = never, 1 = default = whenever it is requested,
            # 2 = when a cursor is created, 4 = when a query is executed, 7 = always

            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            database='newflask',
            charset='utf8'
        )

    def connect(self):
        """建立连接"""
        conn = self.pool.connection()
        cursor = conn.cursor()
        return conn, cursor

    def close(self, conn, cursor):
        """关闭连接"""
        cursor.close()
        conn.close()

    def fetchone(self, sql, *args):
        """获取单条数据"""
        conn, cursor = self.connect()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        self.close(conn, cursor)
        return result

    def fetchall(self, sql, *args):
        """获取所有数据"""
        conn, cursor = self.connect()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        self.close(conn, cursor)
        return result


# 声明一个对象 确保每次引入的是同一个对象(单例)
db = SqlHelper()
