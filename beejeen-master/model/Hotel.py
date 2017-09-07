#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

from Data import Data


class Hotel(Data):
    def __init__(self, pname = '',pparamForWechat = '', pname_en = '', pname_cn = '', pintro_cn = '', pcountry = '', pcity = ''):
        super(Hotel, self).__init__(pname, pparamForWechat, pname_en, pname_cn, pintro_cn, pcountry, pcity)

    def add(self):
        ids = self.getCountryidAndCityid()
        query = 'insert into Activity (name_en, name_cn, intro_cn, countryid, cityid) values ("' + self.name_en + '", "' + self.name_cn + '", "' + self.intro_cn + '", ' + str(ids[0]) + ', ' + str(ids[1]) + ');'
        return self.condb.commit(query)

    def getJson(self, lang):
        try:
            query = 'update Hotel set view = view + 1 where name_en = \"' + self.name + '\" or name_cn = \"' + self.name + '\";'
            self.condb.commit(query)
            query = 'select * from Hotel where name_cn = \"' + self.name + '\" or name_en = \"' + self.name + '\";'
            res = self.condb.executeCurDictFetchOne(query)
            media = res['video_link']
            if not media:
                media = res['img_link']
            data = {}
            data['iframe_link'] = media + '?poi=4' + str(res['id']) + '&v=' + Data.getVersionCode()
            music = res['music_link']
            if not music is None:
                data['music'] = music
            data['like'] = res['adore']
            en = {}
            en['name'] = res['name_en']
            en['address'] = res['address']
            en['view'] = res['view']
            en['middle'] = []
            en['middle'].append({'icon': 'star', 'text': res['starRating']})
            en['middle'].append({'icon': 'room', 'text': res['numOfRoom']})
            en['middle'].append({'icon': 'rank', 'text': res['rank']})
            en['middle'].append({'icon': 'score', 'text': res['point']})
            en['content'] = []
            en['content'].append({'title': 'introduction', 'text': self.convertEOL(res['intro_en'])})
            en['bottom'] = []
            en['bottom'].append('telephone: ' + res['telephone'])
            en['bottom'].append('website: ' + res['website'])
            en['bottom'].append('type: ' + res['type'])

            cn = {}
            cn['name'] = res['name_cn']
            cn['address'] = res['address']
            cn['view'] = res['view']
            cn['middle'] = []
            cn['middle'].append({'icon': 'star', 'text': res['starRating']})
            cn['middle'].append({'icon': 'room', 'text': res['numOfRoom']})
            cn['middle'].append({'icon': 'rank', 'text': res['rank']})
            cn['middle'].append({'icon': 'score', 'text': res['point']})
            cn['content'] = []
            cn['content'].append({'title': '介绍', 'text': self.convertEOL(res['intro_cn'])})
            cn['bottom'] = []
            cn['bottom'].append('电话: ' + res['telephone'])
            cn['bottom'].append('网址: ' + res['website'])
            cn['bottom'].append('类型: ' + res['type'])
            data['introduction'] = {'en': en, 'cn': cn}
        except Exception as e:
            print('EXCEPTION FROM Hotel getJson:')
            print(e)
        return data
