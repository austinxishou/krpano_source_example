#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-


import re

import tornado.web


pattern = re.compile(r'^m.*')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            print('IndexHandler')
            print(self.request.uri)
            match = pattern.match(self.request.host)
            if match:
                print('this is mobile')
                self.render("../mobile/index.html")
            else:
                print('this is PC')
                self.render("../beejeen/index.html")
        except Exception as e:
            print('EXCEPTION FROM IndexHandler get:')
            print(e)
