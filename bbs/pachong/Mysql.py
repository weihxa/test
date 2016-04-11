#!/usr/bin/env python
#coding:utf-8

import MySQLdb
import conf

class MysqlHelper(object):

    def __init__(self):
        self.__conn_dict = conf.conn_dict

    def In_sql(self,sql):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor()
        #cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        reCount = cur.execute(sql)
        data = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return data