#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import time
import json
import urllib.parse
import tornado.escape
import urllib.request

sys.path.append('/var/server/beejeen/model')


class mWechatLoginHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('mWechatLoginHandler')
            print(self.request.uri)

            #####url = self.get_argument('url')

            url = 'http://m.beejeen.com/html/tour.html?Sight&key=Castle%20Hill'
            url = urllib.parse.quote(url)
            target = 'http://m.beejeen.com/wechatauth?url=' + str(url)


            self.redirect('https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx325ed9b7c056a449&redirect_uri=' + target + '&response_type=code&scope=snsapi_base&state=123#wechat_redirect')
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM mWechatLoginHandler get:')
            print(e)
            self.write('1')


            #self.redirect('https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx325ed9b7c056a449&redirect_uri=http://cps.dianping.com/weiXinRedirect&response_type=code&scope=snsapi_userinfo&state=type%3Dquan%2Curl%3Dhttp%3A%2F%2Fmm.dianping.com%2Fweixin%2Faccount%2Fhome')
