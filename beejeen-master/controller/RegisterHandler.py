#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape
import hashlib

sys.path.append('/var/server/beejeen/model')

from RegisterUser import RegisterUser


class RegisterHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Access-Control-Allow-Headers', 'origin, x-csrftoken, content-type, accept')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def post(self, path):
        try:
            print('RegisterHandler')
            print(self.request.uri)
            print(self.request.body)
            telephone = self.get_body_argument('telephone')
            name = self.get_body_argument('name')
            password = self.get_body_argument('password')
            registerUser = RegisterUser(telephone, name, password)
            self.write(str(registerUser.register()))
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM RegisterHandler post:')
            print(e)
            self.write('4')
