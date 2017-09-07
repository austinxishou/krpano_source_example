#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from Look import Look


def getLook(lang):
    try:
        result = Look().getJson(lang)
        print(result)
    except Exception as e:
        print('EXCEPTION FROM getLook:')
        print(e)
    return result


class LookHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('LookHandler')
            print(self.request.uri)
            print('val is look')
            self.write(getLook(self.get_argument('lang')))
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM LookHandler get:')
            print(e)
