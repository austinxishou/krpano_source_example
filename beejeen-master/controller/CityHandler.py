#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import re
import sys

import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from City import City
from ThumbCity import ThumbCity
from mThumbCity import mThumbCity


def getPointsFromCity(cityName, lang, device):
    try:
        if device == 'm':
            city = mThumbCity(cityName)
        else:
            city = ThumbCity(cityName)
        result = city.getJson(lang)
        print(result)
    except Exception as e:
        print('EXCEPTION FROM getPointsFromCity:')
        print(e)
    return result


class CityHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('CityHandler')
            print(self.request.uri)
            print(self.get_argument('key'))
            #val = urllib.parse.unquote(self.get_argument('key'))
            val = tornado.escape.url_unescape(self.get_argument('key'))
            print('val is ' + val)
            referer = self.request.headers.get('Referer')
            try:
                lang = re.search(r'-(.*)\..*', referer).group(1)
            except:
                lang = 'cn'
            if City.isCity(val):
                print('content city is ' + val)
                self.write(getPointsFromCity(val, lang, self.request.host.split(".")[0]))
            else:
                print('404 not found ' + val)
                self.write('{"link":"http://' + self.request.host + '/html/404.html"}')
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM CityHandler get:')
            print(e)
