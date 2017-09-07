#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import re
import sys
import tornado.web

import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from Country import Country
from ThumbCountry import ThumbCountry


def getCitiesFromCountry(countryName, lang):
    try:
        country = ThumbCountry(countryName)
        result = country.getJson(lang)
        print(result)
    except Exception as e:
        print('EXCEPTION FROM getCitiesFromCountry:')
        print(e)
    return result


class CountryHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('CountryHandler')
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
            if Country.isCountry(val):
                print('content country is ' + val)
                self.write(getCitiesFromCountry(val, lang))
            else:
                print('404 not found ' + val)
                self.write('{"link":"http://' + self.request.host + '/html/404.html"}')
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM CountryHandler get:')
            print(e)

