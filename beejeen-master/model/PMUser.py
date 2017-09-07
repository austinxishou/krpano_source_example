#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

from ConnectionDB import ConnectionDB


class PMUser:
    def __init__(self, pname, ppassword):
        self.condb = ConnectionDB()
        self.name = pname
        self.password = ppassword

    def authenticate(self):
        try:
            query = 'select * from PMUser;'
            res = self.condb.executeCurDictFetchOne(query)
            if self.name == res['name'] and self.password == res['password']:
                return True
        except Exception as e:
            print('EXCEPTION FROM PMUser authenticate:')
            print(e)
        return False

