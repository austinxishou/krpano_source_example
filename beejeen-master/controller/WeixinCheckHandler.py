#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web
import hashlib

import urllib.parse
import tornado.escape


class WeixinCheckHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('WeixinCheckHandler')
            print(self.request.uri)
            signature = self.get_argument('signature')
            timestamp = self.get_argument('timestamp')
            nonce = self.get_argument('nonce')
            echostr = self.get_argument('echostr')

            token = 'beejeen20151224BJ'

            liste = [token.encode('utf-8'), timestamp.encode('utf-8'), nonce.encode('utf-8')]
            
            liste.sort()
            sha1 = hashlib.sha1()
            liste = list(map(sha1.update, liste))
            hashcode = sha1.hexdigest()
            if hashcode == signature:
                self.write(echostr)
            else:
                self.write("")
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM CheckTelephoneHandler get:')
            print(e)
            self.write('1')
