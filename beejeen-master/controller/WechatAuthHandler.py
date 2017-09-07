#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import time
import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from WechatUser import WechatUser


class WechatAuthHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('WechatAuthHandler')
            print(self.request.uri)
            target = str(self.get_argument('url'))
            #url = self.get_argument('urlrefer')
            userinfo = WechatUser.getUserInfo(self.get_argument('code'))
            user = WechatUser(userinfo['openid'], userinfo['nickname'], userinfo['headimgurl'])
            user.add()
            target = urllib.parse.unquote(target) + '&user=' + userinfo['nickname'] + '&profile=' + userinfo['headimgurl'] + '&userid=' + str(WechatUser.getId(userinfo['openid']))
            self.redirect(target)
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM WechatAuthHandler get:')
            print(e)
            self.write('1')
