#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-


################# aiomyslq is necessary as it is async
################# pymysql is sync and tornado is single thread so it's dangerous
import pymysql


class ConnectionDB:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='password', db='dbbj', charset='utf8')
        self.curDict = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.curDict.close()
        self.cur.close()
        self.conn.close()

    def executeCurFetchOne(self, query):
        self.cur.execute(query)
        return self.cur.fetchone()

    def executeCurFetchAll(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def executeCurDictFetchOne(self, query):
        self.curDict.execute(query)
        return self.curDict.fetchone()

    def executeCurDictFetchAll(self, query):
        self.curDict.execute(query)
        return self.curDict.fetchall()

    def commit(self, query):
        self.cur.execute(query)
        self.conn.commit()
