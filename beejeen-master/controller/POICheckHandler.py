#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape

from City import City


class POICheckHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('POICheckHandler')
            print(self.request.uri)
            val = tornado.escape.url_unescape(self.get_argument('key'))
            msg = urllib.parse.unquote(val)
            self.write(City.getCitiesOfCountry(msg))
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM POICheckHandler get:')
            print(e)
