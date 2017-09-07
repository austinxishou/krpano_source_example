#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import hashlib

from ConnectionDB import ConnectionDB


class Comment:
    def __init__(self, pcontent, puserid, ppoi, path, patv, pscene):
        self.condb = ConnectionDB()
        self.content = pcontent
        self.userid = puserid
        self.poi = ppoi
        self.ath = path
        self.atv = patv
        self.scene = pscene

    def add(self):
        try:
            query = 'insert into Comment (userid, content, ath, atv, scene, POICode) values (' + str(self.userid) + ', \'' + str(self.content) + '\', ' + str(self.ath) + ', ' + str(self.atv) + ', \'' + self.scene + '\', ' + str(self.poi) + ');'
            self.condb.commit(query)
        except Exception as e:
            print('EXCEPTION FROM Comment add:')
            print(e)

    def get(poicode, pscene):
        data = {}
        try:
            query = 'select Comment.*, User.name, User.profile from Comment left join User on User.id = Comment.userid where Comment.POICode = ' + str(poicode) + ' and Comment.scene = \'' + pscene + '\';'
            condb = ConnectionDB()
            res = condb.executeCurDictFetchAll(query)
            data['comment'] = []
            for t in res:
                data['comment'].append({'id':t['id'], 'profile':t['profile'], 'name':t['name'], 'ath':t['ath'], 'atv':t['atv'], 'content':t['content']})
        except Exception as e:
            print('EXCEPTION FROM Comment get:')
            print(e)
        return data

