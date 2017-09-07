#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

from ConnectionDB import ConnectionDB
from Data import Data


class City(Data):
    def __init__(self, pname, pparamForWechat = ''):
        super(City, self).__init__(pname)
        self.paramForWechat = pparamForWechat

    def getJson(self, lang):
        try:
            query = 'select * from City where name_cn = \"' + self.name + '\" or name_en = \"' + self.name + '\";'
            res = self.condb.executeCurDictFetchOne(query)
            media = res['video_link']
            if not media:
                media = res['img_link']
            music = res['music_link']
            data = {}
            data['iframe_link'] = media + '?poi=2' + str(res['id']) + '&v=' + Data.getVersionCode()
            if not music is None:
                data['music'] = music
            data['like'] = res['adore']
            en = {}
            en['name'] = res['name_en']
            cn = {}
            cn['name'] = res['name_cn']
            data['introduction'] = {'en': en, 'cn': cn}
        except Exception as e:
            print('EXCEPTION FROM City getJson:')
            print(e)
        return data

    def isCity(val):
        try:
            query = 'select count(*) from City where name_en = \"' + val + '\" or name_cn = \"' + val + '\";'
            condb = ConnectionDB()
            res = condb.executeCurFetchOne(query)
        except Exception as e:
            print('EXCEPTION FROM isCity:')
            print(e)
            return False
        if res[0] > 0:
            return True
        return False

    def getCitiesOfCountry(countryName):
        try:
            query = 'select name_cn from City where City.countryid = (select id from Country where name_cn = \'' + countryName + '\');'
            condb = ConnectionDB()
            res = condb.executeCurDictFetchAll(query)
            data = {}
            data['city'] = []
            data['city'].append('未选择')
            for t in res:
                data['city'].append(t['name_cn'])
        except Exception as e:
            print('EXCEPTION FROM Country getJson:')
            print(e)
        return data

