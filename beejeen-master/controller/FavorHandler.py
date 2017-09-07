#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web
import urllib.parse

sys.path.append('/var/server/beejeen/model')

from Activity import Activity
from Restaurant import Restaurant
from Hotel import Hotel
from Sight import Sight
from Travel import Travel


class FavorHandler(tornado.web.RequestHandler):
    def post(self, path):
        try:
            print(self.request.body)
            data = eval(str(self.get_body_argument("type")) + '("' + self.get_body_argument("key") + '")')
            data.doFavor()
        except Exception as e:
            print('EXCEPTION FROM FavorHandler post:')
            print(e)
