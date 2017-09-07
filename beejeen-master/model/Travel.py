#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import json
from WechatToken import WechatToken
from Data import Data



class Travel(Data):
    def __init__(self, pname, pparamForWechat):
        super(Travel, self).__init__(pname)
        self.paramForWechat = pparamForWechat

    def getJson(self, lang):
        try:
            query = 'select * from Travel where name_en = \"' + self.name + '\" or name_cn = \"' + self.name + '\";'
            #query = 'select t.* from Country c left join RelationCountryTravel rct on c.id=rct.countryid left join Travel t on t.id = rct.travelid where t.name_en = \"' + self.name + '\" or t.name_cn = \"' + self.name + '\"'
            resTravel = self.condb.executeCurDictFetchOne(query)
            query = 'select * from InfoTravel where id = ' + str(resTravel['infoid']) + ';'
            resInfoTravel = self.condb.executeCurDictFetchOne(query)
            query = 'select * from Country where id = (select countryid from RelationCountryTravel where travelid = ' + str(resTravel['id']) + ')'
            resCountry = self.condb.executeCurDictFetchAll(query)
            nameCountrys = ''
            for res in resCountry:
                nameCountrys += (res['name_cn'] + ' ')
            content = ''
            with open('/var/server/beejeen/sql/travel/' + resTravel['name_en'] + '.json', 'r') as json_data:
                content = json.load(json_data)
            data = {}
            data['name'] = resTravel['name_cn']
            data['cost'] = resTravel['cost_cn']
            data['cost_detail'] = self.convertEOL(resTravel['cost_detail_cn']).replace(" ", "&nbsp;")
            data['img'] = resTravel['thumb_mobile_link']  # mobile needs it
            s = WechatToken('http://m.beejeen.com/html/itinerary.html?' + self.paramForWechat)
            data['weixin'] = s.sign()
            data['weixin']['intro'] = resTravel['highlight_cn']
            # 行程总览 < --- coming from db
            data['content'] = []
            data['content'].append({'middle':[], 'right':[]})
            data['content'][0]['middle'].append({"icon": "highlight", "text": "行程亮点"})
            data['content'][0]['middle'].append({"icon": "tips", "text": "旅行提示"})
            data['content'][0]['middle'].append({"icon": "visa", "text": "护照签证"})
            data['content'][0]['middle'].append({"icon": "list", "text": "物品清单"})
            data['content'][0]['middle'].append({"icon": "surprise", "text": "报名方式"})
            data['content'][0]['right'].append({"text":{"title":"行程亮点","content":self.convertEOL(resTravel['highlight_cn'])}})
            data['content'][0]['right'].append({"text":{"title":"旅行提示","content":self.convertEOL(resTravel['notice_cn'])}})
            data['content'][0]['right'].append({"text":{"title":"护照签证","content":self.convertEOL(resInfoTravel['passport_cn'])}})
            data['content'][0]['right'].append({"text":{"title":"物品清单","content":self.convertEOL(resInfoTravel['accessory_cn'])}})
            data['content'][0]['right'].append({"text":{"title":"报名方式","content":self.convertEOL(resTravel['signup_cn'])}})
            # days <--- coming from json file
            cnt = content['content']
            data['days'] = len(cnt)
            data['country'] = nameCountrys
            for i in range(0, len(cnt)):
                for j in range(0, len(cnt[i]['middle'])):
                    icon = cnt[i]['middle'][j]['icon']
                    if icon != 'flight' and icon != 'car' and icon != 'tips':
                        query = 'select * from ' + icon.title() + ' where name_en = \"' + cnt[i]['middle'][j]['text'] + '\";'
                        res = self.condb.executeCurDictFetchOne(query)
                        if not res:
                            continue
                        name_en = res['name_en']
                        name_cn = res['name_cn']
                        if not name_cn:
                            name_cn = name_en
                        media = res['video_link']
                        if not media:
                            media = res['img_link']
                        cnt[i]['right'][j]['sight']['name'] = name_cn
                        cnt[i]['right'][j]['sight']['intro'] = res['intro_cn']
                        cnt[i]['right'][j]['sight']['img'] = res['thumb_link']
                        if not media is None:
                            key = str(name_cn).replace("&", "|")
                            cnt[i]['right'][j]['sight']['href'] = 'tour.html?' + icon.title() + '&key=' + key
                        cnt[i]['middle'][j]['text'] = name_cn
                data['content'].append(cnt[i])
            jsondata = json.dumps(data, ensure_ascii=False)
        except Exception as e:
            print('EXCEPTION FROM Travel getJson:')
            print(e)
        return jsondata
