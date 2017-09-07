#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from Travel import Travel


def getTravel(val, valWithWechat):
    try:
        obj = Travel(val, valWithWechat)
        result = obj.getJson('set lang here')
        print(result)
    except Exception as e:
        print('EXCEPTION FROM getTravel:')
        print(e)
    return result


class TravelHandler(tornado.web.RequestHandler):
    ###############################
    ### post is to build travel ###
    ###############################
    def post(self, path):
        try:
            print('TravelHandler')
            #print(self.request.body)
            print(self.get_argument('title'))
            print(self.get_argument('author'))
            print(self.request.files['backgroundImage'][0]['filename'])
            img = self.request.files['backgroundImage'][0]['body']
            test = open('test.png', 'wb+')
            test.write(img)
            test.close()
            #self.set_status(404)
            #self.set_status(200)
            self.write('success')
        except Exception as e:
            print('EXCEPTION FROM TravelHandler post:')
            print(e)

    def get(self, path):
        try:
            print('TravelHandler')
            print(self.request.uri)
            print(self.get_argument('key'))
            val = tornado.escape.url_unescape(self.get_argument('key'))
            val = val.split("=", 1)[0]
            val = val.split("&", 1)[0]
            #val = val.replace('|', '&')
            print('val is ' + val)
            print('val with wechat is ' + self.get_argument('key'))
            self.write(getTravel(val, self.get_argument('key')))
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM TravelHandler get:')
            print(e)
