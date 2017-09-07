#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import tornado.web

import urllib.parse
import tornado.escape

from Comment import Comment

class AddCommentHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Access-Control-Allow-Headers', 'origin, x-csrftoken, content-type, accept')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Allow-Credentials', True)

        self.set_header('Content-type', 'application/json')

    def post(self, path):
        try:
            print('AddCommentHandler')
            print(self.request.uri)
            content = self.get_body_argument('content')
            userid = self.get_body_argument('userid')
            poi = self.get_body_argument('poi')
            ath = self.get_body_argument('ath')
            atv = self.get_body_argument('atv')
            scene = self.get_body_argument('scene')
            comment = Comment(content, userid, poi, ath, atv, scene)
            comment.add()
            print(self.request.cookies)
            print(self.get_secure_cookie("user"))
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM AddCommentHandler post:')
            print(e)
            self.write('1')
        else:
            self.write('0')
