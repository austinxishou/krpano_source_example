#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

from ConnectionDB import ConnectionDB
from Data import Data


class Country(Data):
    def __init__(self, pname, pparamForWechat = ''):
        super(Country, self).__init__(pname)
        self.paramForWechat = pparamForWechat

    def getJson(self, lang):
        try:
            query = 'select * from Country where name_cn = \"' + self.name + '\" or name_en = \"' + self.name + '\";'
            res = self.condb.executeCurDictFetchOne(query)
            media = res['video_link']
            if not media:
                media = res['img_link']
            data = {}
            data['iframe_link'] = media + '?poi=1' + str(res['id']) + '&v=' + Data.getVersionCode()
            music = res['music_link']
            if not music is None:
                data['music'] = music
            data['like'] = res['adore']
            en = {}
            en['name'] = res['name_en']
            cn = {}
            cn['name'] = res['name_cn']
            data['introduction'] = {'en': en, 'cn': cn}
        except Exception as e:
            print('EXCEPTION FROM Country getJson:')
            print(e)
        return data


    def isCountry(val):
        try:
            query = 'select count(*) from Country where name_en = \"' + val + '\" or name_cn = \"' + val + '\";'
            condb = ConnectionDB()
            res = condb.executeCurFetchOne(query)
        except Exception as e:
            print('EXCEPTION FROM isCountry:')
            print(e)
            return False
        if res[0] > 0:
            return True
        return False

    def getAllCountries():
        try:
            query = 'select name_cn from Country;'
            condb = ConnectionDB()
            res = condb.executeCurDictFetchAll(query)
            data = {}
            data['country'] = []
            data['country'].append('未选择')
            for t in res:
                data['country'].append(t['name_cn'])
        except Exception as e:
            print('EXCEPTION FROM Country getJson:')
            print(e)
        return data

