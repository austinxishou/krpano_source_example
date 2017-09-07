#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-


import time
import random
import string
import hashlib
import json
import urllib.request

from ConnectionDB import ConnectionDB


class WechatToken:
    def __init__(self, url):
        try:
            query = 'select * from WechatToken;'
            condb = ConnectionDB()
            res = condb.executeCurDictFetchOne(query)
            ticket = res['ticket']
            nonceStr = res['nonceStr']
            timestamp = res['timestamp']
            if not ticket:
                token = urllib.request.urlopen('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx325ed9b7c056a449&secret=a3552bddd92734e695c9372f54582cee').read().decode('utf-8')
                jsontoken = json.loads(token)
                ticket = urllib.request.urlopen('https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=' + jsontoken['access_token'] + '&type=jsapi').read().decode('utf-8')
                jsonticket = json.loads(ticket)
                timestamp = str(self.__create_timestamp())
                nonceStr = self.__create_nonce_str()
                query = 'update WechatToken set token = \"' + jsontoken['access_token'] + '\"; update WechatToken set ticket = \"' + jsonticket['ticket'] + '\"; update WechatToken set timestamp = \"' + timestamp + '\"; update WechatToken set nonceStr = \"' + nonceStr + '\";'
                condb.commit(query)
                ticket = jsonticket['ticket']
            self.ret = {
                'jsapi_ticket': ticket,
                'nonceStr': nonceStr,
                'timestamp': timestamp,
                'url': url
            }
        except Exception as e:
            print('EXCEPTION FROM WeChatToken constructor:')
            print(e)

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def sign(self):
        try:
            string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
            #self.ret['signature'] = hashlib.sha1(string).hexdigest()
            self.ret['signature'] = hashlib.sha1(string.encode('utf-8')).hexdigest()
            del self.ret['jsapi_ticket']
            self.ret['appId'] = 'wx325ed9b7c056a449'
        except Exception as e:
            print('EXCEPTION FROM WechatToken sign:')
            print(e)
        return self.ret

