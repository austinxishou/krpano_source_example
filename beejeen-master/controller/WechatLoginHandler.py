#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import time
import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from WechatUser import WechatUser

class WechatLoginHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('WechatLoginHandler')
            print(self.request.uri)
            #url = self.request.headers.get("Referer")
            url = urllib.parse.quote(self.get_argument('url'))
            target = 'http://www.beejeen.com/wechatauth?url=' + str(url)
            self.redirect(WechatUser.getUrl(str(target)))
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM WechatLoginHandler get:')
            print(e)
            self.write('1')

