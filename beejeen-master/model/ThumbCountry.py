#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

from Data import Data
from ConnectionDB import ConnectionDB

class ThumbCountry(Data):
    def __init__(self, pname):
        super(ThumbCountry, self).__init__(pname)
        
    def getJson(self, lang):
        try:
            query = 'select * from Country where name_en = \"' + self.name + '\" or name_cn = \"' + self.name + '\";'
            resCountry = self.condb.executeCurDictFetchOne(query)
            query = 'select * from City where countryid = ' + str(resCountry['id']) + ' and thumb_link != \'\' and thumb_link is not null' + ';'
            resCities = self.condb.executeCurDictFetchAll(query)
            query = 'select * from Travel where id = (select travelid from RelationCountryTravel where countryid = ' + str(resCountry['id']) + ');'
            #query = 'select t.* from Country c left join RelationCountryTravel rct on c.id=rct.countryid left join Travel t on t.id = rct.travelid where c.id=' + str(resCountry['id'])
            resTravel = self.condb.executeCurDictFetchAll(query)
            query = 'select * from Continent;'
            resContinent = self.condb.executeCurDictFetchAll(query)
            data = {}
            data['navigation'] = []
            i = 0
            for res in resContinent:
                query = 'select name_' + lang + ' from Country where continentid = ' + str(res['id']) + ';'
                tmp = self.condb.executeCurFetchAll(query)
                arr = []
                for t in tmp:
                    arr.append(t[0])
                data['navigation'].append({})
                data['navigation'][i]['name'] = res['name_' + lang]
                data['navigation'][i]['item'] = arr
                i += 1

            data['country'] = {'name' : resCountry['name_' + lang]}
            data['country']['text'] = self.convertEOL(resCountry['text_' + lang])
            data['country']['iframe_type'] = 'Country'
            data['country']['iframe_link'] = resCountry['rep_link']
            if len(resTravel) > 0:
                for travel in resTravel:
                    del travel['ad_cost']
                    travel['cost'] = travel['cost_cn']
                    del travel['cost_cn']
                    #travel['intro'] = self.convertEOL(travel['highlight_' + lang])
                    travel['intro'] = self.convertEOL(travel['highlight_' + 'cn'])
                    del travel['highlight_cn']
                    del travel['notice_cn']
                    travel['img'] = travel['thumb_link']
                    del travel['thumb_link']
                    travel['like'] = travel['adore']
                    del travel['adore']
                    travel['name'] = travel['name_' + lang]
                    del travel['name_en']
                    del travel['name_cn']
                    travel['country'] = str(resCountry['name_cn'])
                    travel['type'] = []
                    travel['type'].append("亲子")
                    travel['type'].append("休闲")
                data['itinerary'] = resTravel
            data['display_append'] = []
            for row in resCities:
                name = row['name_' + lang]
                text = self.convertEOL(row['text_' + lang])
                tmp = {}
                tmp['id'] = row['id']
                tmp['type'] = 'City'
                tmp['img'] = row['thumb_link']
                tmp['name'] = name
                tmp['text'] = text
                data['display_append'].append(tmp)
        except Exception as e:
            print('EXCEPTION FROM ThumbCountry getJson:')
            print(e)
        return data
