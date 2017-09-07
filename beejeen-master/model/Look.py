#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import json
from Data import Data


class Look(Data):
    def __init__(self):
        super(Look, self).__init__()

    def getJson(self, lang):
        try:
            query = 'select * from Chosen;'
            resChosen = self.condb.executeCurDictFetchAll(query)
            query = 'select * from Country where ad_cost > 0 order by ad_cost desc;'
            resCountry = self.condb.executeCurDictFetchAll(query)
            query = 'select * from Travel where ad_cost > 0 order by ad_cost desc;'
            resTravel = self.condb.executeCurDictFetchAll(query)
            query = 'select * from Continent;'
            resContinent = self.condb.executeCurDictFetchAll(query)
            data = {}
            data['header'] = []
            data['country'] = []
            data['itinerary'] = []
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

            i = 0
            for res in resChosen:
                data['header'].append({})
                data['header'][i]['img'] = res['thumb_link']
                data['header'][i]['img_mobile'] = res['thumb_mobile_link']
                data['header'][i]['a-href'] = 'tour.html?' + res['type'] + '&key=' + res['name_en'].replace("&", "|")
                query = 'select * from ' + res['type'] + ' where name_en = \"' + res['name_en'] + '\";'
                resPoint = self.condb.executeCurDictFetchOne(query)
                data['header'][i]['title'] = resPoint['name_cn']
                query = 'select Country.name_cn as country_name, City.name_cn as city_name from Country inner join City on Country.id = (select countryid from ' + res['type'] + ' where name_en = \"' + res['name_en'] + '\") and City.id = (select cityid from ' + res['type'] + ' where name_en = \"' + res['name_en'] + '\");'
                resCC = self.condb.executeCurDictFetchOne(query)
                data['header'][i]['text'] = resCC['country_name'] + '|' + resCC['city_name']
                i += 1

            i = 0
            for res in resCountry:
                data['country'].append({})
                data['country'][i]['img'] = res['thumb_link']
                data['country'][i]['name'] = res['name_' + lang]
                data['country'][i]['a-href'] = 'country-' + lang + '.html?' + res['name_' + lang]
                i += 1

            i = 0
            for res in resTravel:
                data['itinerary'].append({})
                data['itinerary'][i]['img'] = res['thumb_link']
                data['itinerary'][i]['title'] = res['name_' + lang]
                data['itinerary'][i]['country'] = 'Sri Lanka' ########### WRONG!!!!!!!
                data['itinerary'][i]['content'] = self.convertEOL(res['highlight_cn'])
                data['itinerary'][i]['cost'] = res['cost_cn']
                data['itinerary'][i]['a-href'] = 'itinerary.html?' + res['name_en']
                i += 1

            jsondata = json.dumps(data, ensure_ascii=False)
        except Exception as e:
            print('EXCEPTION FROM Look getJson:')
            print(e)
        return jsondata
