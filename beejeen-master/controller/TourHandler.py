#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from Country import Country
from City import City
from Activity import Activity
from Restaurant import Restaurant
from Hotel import Hotel
from Sight import Sight


# valWithWechat is for wechat share
def getPointInfo(val, pointType, valWithWechat):
    try:
        obj = eval(str(pointType) + '("' + str(val) + '","' + valWithWechat + '")')
        result = obj.getJson('set lang here')
        print(result)
    except Exception as e:
        print('EXCEPTION FROM getPointInfo:')
        print(e)
    return result


class TourHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('TourHandler')
            print(self.request.uri)
            print(self.get_argument('key'))
            #val = urllib.parse.unquote(self.get_argument('key'))
            val = tornado.escape.url_unescape(self.get_argument('key'))
            pointType = self.get_argument('type')
            print('type is ' + pointType)
            val = val.replace('|', '&')
            print('val is ' + val)
            self.write(getPointInfo(val, pointType, self.get_argument('key')))
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM TourHandler get:')
            print(e)
