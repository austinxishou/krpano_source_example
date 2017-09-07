#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape


class PMHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('PMHandler')
            print(self.request.uri)
            #self.render("../beejeen/html/bjlogin.html")
            self.redirect("http://www.beejeen.com/bjloginpage")
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM LookHandler get:')
            print(e)
