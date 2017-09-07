#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-


import re
import tornado.web

import urllib.parse


pattern = re.compile(r'^m.*')

class PageHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('PageHandler: ' + path)
            match = pattern.match(self.request.host)
            if match:
                print('this is mobile')
                self.render("mobile/" + urllib.parse.unquote(path))
            else:
                print('this is PC')
                self.render("beejeen/" + urllib.parse.unquote(path))
        except Exception as e:
            print('EXCEPTION FROM PageHandler get:')
            print(e)
