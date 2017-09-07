#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

from Data import Data


class CityItem(Data):
    def __init__(self, pname, pitem):
        super(CityItem, self).__init__(pname)
        self.item = pitem

    def getJson(self, lang):
        try:
            data = {}
            query = 'select * from ' + self.item + ' where cityid = (select id from City where name_cn = \"' + self.name + '\" or name_en = \"' + self.name + '\") and thumb_link is not null and thumb_link != \'\' and (img_link is not null and img_link != \'\' or video_link is not null and video_link != \'\');'
            res = self.condb.executeCurDictFetchAll(query)
            data['item'] = []
            for row in res:
                # 若图与视频同时存在，则media置为视频
                media = row['video_link']
                if not media:
                    media = row['img_link']
                if not media:
                    continue
                thumb = row['thumb_link']
                if thumb is None:
                    continue
                tmp = {}
                tmp['id'] = row['id']
                tmp['table'] = self.item
                tmp['img'] = '\'' + thumb + '\''
                tmp['name'] = row['name_' + lang]
                data['item'].append(tmp)
        except Exception as e:
            print('EXCEPTION FROM CityItem getJson:')
            print(e)
        return data
