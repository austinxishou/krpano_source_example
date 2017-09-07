#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import re
import sys
import tornado.web
import base64

import urllib.parse
import tornado.escape

sys.path.append('/var/server/beejeen/model')

from Country import Country
from City import City


patternDefense = re.compile(r'.*(create |select |update |alter |delete |drop |show |having | or |<.*>|/).*', re.IGNORECASE)
# 首页搜索内容点击后跳转
class SearchHandler(tornado.web.RequestHandler):
    def get(self, path):
        try:
            print('SearchHandler')
            print(self.request.uri)
            print(self.get_argument('key'))
            #val = urllib.parse.unquote(self.get_argument('key'))
            val = tornado.escape.url_unescape(self.get_argument('key'))

            #bytesString = val.encode(encoding="utf-8")
            #decodestr = base64.b64decode(bytesString)
            #print('aaaaaaaaaaaaaaaaa')
            #print(len(decodestr.decode()))  # 'hello world'
            #print('bbbbbbbbbbbbbbbbb')
            #if len(decodestr.decode()) != 0:
                #val = decodestr.decode()


            # remove ';' from val if exists
            # otherwise, 'select * from mytable where mycolumn = abc;def' will produce an error coming from 'def', which can't be caught by try...catch...
            val = val.replace(";", "")
            if not val:
                return
            matchDefense = patternDefense.match(val)
            if matchDefense:
                # WARNING!!!
                # someone is trying to do web injection attacks
                self.write('{"link":"https://image.baidu.com/search/detail?ct=503316480&z=&tn=baiduimagedetail&ipn=d&word=%E6%89%93%E5%87%BB%E9%BB%91%E5%AE%A2&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=-1&cs=623464961,1255249105&os=4288987045,2593232107&simid=3471060388,531993260&pn=1&rn=1&di=35735023170&ln=1963&fr=&fmq=1497945237455_R&fm=result&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&is=0,0&istype=2&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=http%3A%2F%2Fwww.17waihui.com%2Fuploadfile%2F2015%2F0720%2F20150720034036427.jpg&rpstart=0&rpnum=0&adpicid=0&ctd=1497945272672^3_1173X680%1"}')
                return
            print('key is ' + val)
            msg = urllib.parse.quote(val)
            head = self.request.headers.get('Origin')
            head = head if head else ("http://" + self.request.host)
            # for search
            # when user is searching some word somewhere, the frontend doesn't know which page should be loaded
            if Country.isCountry(val):
                print('link to new page: country is ' + val)
                self.write('{"link":"http://' + self.request.host + '/html/country.html?' + msg + '"}')
            elif City.isCity(val):
                print('link to new page: city is ' + val)
                self.write('{"link":"http://' + self.request.host + '/html/city.html?' + msg + '"}')
            else:
                self.write('{"link":"http://' + self.request.host + '/html/404.html"}')
                print('404 not found ' + val)
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM SearchHandler get:')
            print(e)
