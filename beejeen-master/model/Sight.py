#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

from Data import Data


class Sight(Data):
    def __init__(self, pname = '',pparamForWechat = '', pname_en = '', pname_cn = '', pintro_cn = '', pcountry = '', pcity = ''):
        super(Sight, self).__init__(pname, pparamForWechat, pname_en, pname_cn, pintro_cn, pcountry, pcity)

    def add(self):
        ids = self.getCountryidAndCityid()
        query = 'insert into Activity (name_en, name_cn, intro_cn, countryid, cityid) values ("' + self.name_en + '", "' + self.name_cn + '", "' + self.intro_cn + '", ' + str(ids[0]) + ', ' + str(ids[1]) + ');'
        return self.condb.commit(query)

    def getJson(self, lang):
        try:
            query = 'update Sight set view = view + 1 where name_en = \"' + self.name + '\" or name_cn = \"' + self.name + '\";'
            self.condb.commit(query)
            query = 'select * from Sight where name_cn = \"' + self.name + '\" or name_en = \"' + self.name + '\";'
            res = self.condb.executeCurDictFetchOne(query)
            media = res['video_link']
            if not media:
                media = res['img_link']
            data = {}
            data['iframe_link'] = media + '?poi=3' + str(res['id']) + '&v=' + Data.getVersionCode()
            music = res['music_link']
            if not music is None:
                data['music'] = music
            data['like'] = res['adore']
            en = {}
            en['name'] = res['name_en']
            en['address'] = res['address']
            en['view'] = res['view']
            en['middle'] = []
            en['middle'].append({'icon': 'time', 'text': res['openDate']})
            en['middle'].append({'icon': 'price', 'text': res['ticket_en']})
            en['middle'].append({'icon': 'rank', 'text': res['rank']})
            en['middle'].append({'icon': 'score', 'text': res['point']})
            en['content'] = []
            en['content'].append({'title': 'introduction', 'text': self.convertEOL(res['intro_en'])})
            en['content'].append({'title': 'Known for', 'text': self.convertEOL(res['knownFor_en'])})
            en['bottom'] = []
            en['bottom'].append('telephone: ' + res['telephone'])
            en['bottom'].append('website: ' + res['website'])
            en['bottom'].append('arrival mode: ' + self.convertEOL(res['arrivalMode']))
            en['bottom'].append('open time: ' + res['openTime'])
            en['bottom'].append('local name: ' + res['name_local'])

            cn = {}
            cn['name'] = res['name_cn']
            cn['address'] = res['address']
            cn['view'] = res['view']
            cn['middle'] = []
            cn['middle'].append({'icon': 'time', 'text': res['openDate']})
            cn['middle'].append({'icon': 'price', 'text': res['ticket_cn']})
            cn['middle'].append({'icon': 'rank', 'text': res['rank']})
            cn['middle'].append({'icon': 'score', 'text': res['point']})
            cn['content'] = []
            cn['content'].append({'title': '介绍', 'text': self.convertEOL(res['intro_cn'])})
            cn['content'].append({'title': '知名', 'text': self.convertEOL(res['knownFor_cn'])})
            cn['bottom'] = []
            cn['bottom'].append('电话: ' + res['telephone'])
            cn['bottom'].append('网址: ' + res['website'])
            cn['bottom'].append('抵达方式: ' + self.convertEOL(res['arrivalMode']))
            cn['bottom'].append('营业时间: ' + res['openTime'])
            cn['bottom'].append('当地名称: ' + res['name_local'])

            data['introduction'] = {'en': en, 'cn': cn}
        except Exception as e:
            print('EXCEPTION FROM Sight getJson:')
            print(e)
        return data
