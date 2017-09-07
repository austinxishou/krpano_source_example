#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import re
import sys

import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from CityItem import CityItem


def getItemPointsFromCity(item, cityName, lang):
    try:
        city = CityItem(cityName, item)
        result = city.getJson(lang)
        print(result)
    except Exception as e:
        print('EXCEPTION FROM getItemPointsFromCity:')
        print(e)
    return result


class CityItemHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('CityItemHandler')
            print(self.request.uri)
            print(self.get_argument('key'))
            #val = urllib.parse.unquote(self.get_argument('key'))
            val = tornado.escape.url_unescape(self.get_argument('key'))
            item = self.get_argument('type')
            print('view point is ' + item)
            referer = self.request.headers.get('Referer')
            try:
                lang = re.search(r'-(.*)\..*', referer).group(1)
            except:
                lang = 'cn'
            val = val.replace('|', '&')
            print('val is ' + val)
            self.write(getItemPointsFromCity(item, val, lang))
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM CityItemHandler get:')
            print(e)
