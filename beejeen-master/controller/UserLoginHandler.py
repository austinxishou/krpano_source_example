#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import time
import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from User import User

class UserLoginHandler(tornado.web.RequestHandler):
    users = []

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Access-Control-Allow-Headers', 'origin, x-csrftoken, content-type, accept')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header("Content-Type", "application/json; charset=UTF-8")


    def post(self, path):
        try:
            print('UserLoginHandler')
            print(self.request.uri)
            telephone = self.get_body_argument("telephone")
            password = self.get_body_argument("password")
            print(telephone)
            print(password)
            user = User(telephone, password)
            if user.authenticate():
                self.set_secure_cookie("user", telephone, expires=time.time()+60)
                UserLoginHandler.users.append(telephone)
                self.write(user.getJson('cn'))
            else:
                self.write('1')
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM UserLoginHandler post:')
            print(e)
            self.write('2')
