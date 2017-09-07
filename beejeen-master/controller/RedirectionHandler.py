#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-


import tornado.web


class RedirectionHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('RedirectionHandler')
            print(self.request.uri)
            self.redirect('http://www.beejeen.com' + self.request.uri) # 'http://' is necessary
        except Exception as e:
            print('EXCEPTION FROM RedirectionHandler get:')
            print(e)

