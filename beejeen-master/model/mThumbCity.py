#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

from Data import Data


class mThumbCity(Data):
    def __init__(self, pname):
        super(mThumbCity, self).__init__(pname)

    def getJson(self, lang):
        try:
            tables = ['Sight', 'Restaurant', 'Hotel', 'Activity']
            query = 'select * from City where name_en = \"' + self.name + '\" or name_cn = \"' + self.name + '\";'
            resCity = self.condb.executeCurDictFetchOne(query)
            data = {}
            data['city'] = {'name' : resCity['name_' + lang]}
            data['city']['iframe_type'] = 'City'
            data['city']['iframe_link'] = resCity['rep_link']
            data['city']['text'] = self.convertEOL(resCity['text_' + lang].replace("&", "|"))
            data['city']['href_name'] = resCity['name_' + lang].replace('&', '|')

            hots = []
            # 若hots为空，则所有内容全部不能呈现，与前端代码解析json的方式有关
            for t in tables:
                query = 'select * from ' + t + ' where cityid = ' + str(resCity['id']) + ' and ad_cost != 0 and thumb_link is not null and thumb_link != \'\' and (img_link is not null and img_link != \'\' or video_link is not null and video_link != \'\');'
                res = self.condb.executeCurDictFetchAll(query)
                for row in res:
                    row['table'] = t
                    hots.append(row)
            hots.sort(key = lambda x: x['ad_cost'], reverse=True)
            data['hot'] = []
            for row in hots:
                # media默认为krpano多图；若图与视频同时存在，则media置为视频
                media = row['video_link']
                media_type_en = 'video'
                media_type_cn = '视频'
                if not media:
                    media = row['img_link']
                    media_type_en = 'imgs'
                    media_type_cn = '图片'
                if not media:
                    continue
                thumb = row['thumb_link']
                if thumb is None:
                    continue
                tmp = {}
                tmp['id'] = row['id']
                tmp['type'] = 'hot'
                tmp['table'] = row['table']
                #tmp['media-type-cn'] = media_type_cn
                #tmp['media-type-en'] = media_type_en
                tmp['img'] = '\'' + thumb + '\''
                #tmp['main-cell-type'] = 'icon-' + row['table']
                #tmp['a-href'] = media
                tmp['name'] = row['name_' + lang]
                tmp['href_name'] = row['name_' + lang].replace("&", "|")
                #tmp['author-en'] = 'BeejeenVR'
                #tmp['author-cn'] = '百见VR'
                tmp['view'] = row['view']
                tmp['like'] = row['adore']
                data['hot'].append(tmp)
            for t in tables:
                data[t.lower()] = []
                query = 'select * from ' + t + ' where cityid = ' + str(resCity['id']) + ' and thumb_link is not null and thumb_link != \'\' and (img_link is not null and img_link != \'\' or video_link is not null and video_link != \'\');'
                res = self.condb.executeCurDictFetchAll(query)
                for row in res:
                    # 若图与视频同时存在，则media置为视频
                    media = row['video_link']
                    media_type_en = 'video'
                    media_type_cn = '视频'
                    if not media:
                        media = row['img_link']
                        media_type_en = 'imgs'
                        media_type_cn = '图片'
                    if not media:
                        continue
                    thumb = row['thumb_link']
                    if thumb is None:
                        continue
                    tmp = {}
                    tmp['id'] = row['id']
                    tmp['type'] = t.lower()
                    tmp['table'] = t
                    #tmp['media-type-en'] = media_type_en
                    #tmp['media-type-cn'] = media_type_cn
                    #tmp['a-href'] = media
                    tmp['href_name'] = row['name_' + lang].replace("&", "|")
                    tmp['img'] = '\'' + thumb + '\''
                    tmp['name'] = row['name_' + lang]
                    #tmp['main-cell-type'] = 'icon-' + t
                    #tmp['author-en'] = 'BeejeenVR'
                    #tmp['author-cn'] = '百见VR'
                    tmp['view'] = row['view']
                    tmp['like'] = row['adore']
                    data[t.lower()].append(tmp)
        except Exception as e:
            print('EXCEPTION FROM ThumbCity getJson:')
            print(e)
        return data
