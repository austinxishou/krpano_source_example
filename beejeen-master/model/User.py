#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import hashlib

from Data import Data
from ConnectionDB import ConnectionDB

class User(Data):
    def __init__(self, ptelephone, ppassword):
        super(User, self).__init__()
        self.telephone = ptelephone
        self.userid = -1
        self.name = ''
        self.profile = ''
        ppassword = ppassword.encode('utf-8')
        m = hashlib.md5()
        m.update(ppassword)
        self.password = m.hexdigest()

    def authenticate(self):
        try:
            query = 'select * from User where telephone = \'' + self.telephone + '\';'
            res = self.condb.executeCurDictFetchOne(query)
            if res and self.password == res['password']:
                self.name = res['name']
                self.userid = res['id']
                self.profile = res['profile']
                return True
        except Exception as e:
            print('EXCEPTION FROM User authenticate:')
            print(e)
        return False

    def getJson(self, lang):
        data = {}
        data['userid'] = self.userid
        data['name'] = self.name
        data['profile'] = self.profile
        return data

    def checkTelephone(telephone):
        query = 'select count(*) from User where telephone = \'' + telephone + '\';'
        condb = ConnectionDB()
        res = condb.executeCurFetchOne(query)
        if res[0] > 0:
            return False
        return True

    def getId(openId):
        pass
