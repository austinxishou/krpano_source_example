#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from PMUser import PMUser

class CommentHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', 'beejeen.com')
        self.set_header('Access-Control-Allow-Methods', 'POST')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Access-Control-Allow-Headers', 'origin, x-csrftoken, content-type, accept')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    def post(self, path):
        try:
            print('CommentHandler')
            print(self.request.uri)
            print(self.get_secure_cookie('user'))
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM CommentHandler get:')
            print(e)
