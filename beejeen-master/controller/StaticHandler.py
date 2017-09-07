#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-


import tornado.web


class StaticHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')

#    def parse_url_path(self, path):
#        print(path)
#        return super(StaticHandler, self).parse_url_path(path)
