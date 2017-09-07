#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape


class LoginPageHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('LoginPageHandler')
            print(self.request.uri)
            if not self.get_secure_cookie('user'):
                self.render('../beejeen/html/pm.html')
                #self.render('../beejeen/html/bjlogin.html')
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM LoginPageHandler get:')
            print(e)
