#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
#-*- coding: UTF-8 -*-


import pymysql


class ConnectionDB:
    def __init__(self):
        self.conn = pymysql.connect(host='www.beejeen.com', user='root', password='password', db='dbbj', charset='utf8', port=3306)
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
