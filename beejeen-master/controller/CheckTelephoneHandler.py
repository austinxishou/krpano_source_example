#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape
import json

from User import User

class CheckTelephoneHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Access-Control-Allow-Headers', 'origin, x-csrftoken, content-type, accept')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Allow-Credentials', True)

        self.set_header('Content-type', 'application/json')

    def get(self, path):
        try:
            print('CheckTelephoneHandler')
            print(self.request.uri)
            telephone = self.get_argument('telephone')
            if User.checkTelephone(telephone):
                self.write('0')
            else:
                self.write('1')
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM CheckTelephoneHandler get:')
            print(e)
            self.write('2')
