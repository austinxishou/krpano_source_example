#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape

from Country import Country


class POICountryHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('POICountryHandler')
            print(self.request.uri)
            self.write(Country.getAllCountries())
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM POICountryHandler get:')
            print(e)
