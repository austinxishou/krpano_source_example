#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import hashlib

from ConnectionDB import ConnectionDB


class RegisterUser:
    def __init__(self, ptelephone, pname, ppassword):
        self.condb = ConnectionDB()
        self.telephone = ptelephone
        self.name = pname
        ppassword = ppassword.encode('utf-8')
        m = hashlib.md5()
        m.update(ppassword)
        self.password = m.hexdigest()

    def register(self):
        try:
            query = 'select count(*) from User where telephone = \'' + self.telephone + '\';'
            res = self.condb.executeCurFetchOne(query)
            if res[0] > 0:
                return 1
            query = 'insert into User (telephone, name, password, profile, type, creation_time, last_login_time) values (\'' + self.telephone + '\',\'' + self.name + '\', \'' + self.password + '\', \'\', ' + '0, 0, 0);'
            self.condb.commit(query)
            return 0
        except Exception as e:
            print('EXCEPTION FROM RegisterUser register:')
            print(e)
            return 2

