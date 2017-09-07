#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import time
import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from PMUser import PMUser

class LoginHandler(tornado.web.RequestHandler):
    def post(self, path):
        try:
            print('LoginHandler')
            print(self.request.uri)
            name = self.get_body_argument("name")
            password = self.get_body_argument("password")
            print(name)
            print(password)
            user = PMUser(name, password)
            if user.authenticate():
                self.set_secure_cookie("user", name, expires=time.time()+60)
                self.render("../beejeen/html/pm.html")
            else:
                self.write("ERROR")
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM LoginHandler post:')
            print(e)
