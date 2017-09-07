#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-


import time
import random
import string
import hashlib
import json
import urllib.request

from weixin.client import WeixinAPI

from ConnectionDB import ConnectionDB
from Data import Data


class WechatUser(Data):
    APP_ID = 'wx1b1ff128177be12b'
    APP_SECRET = 'c5659616fd6ff10851f2267313f3116b'
    scope = ("snsapi_login", )
    api = None

    def getUrl(url):
        WechatUser.api = WeixinAPI(appid=WechatUser.APP_ID, app_secret=WechatUser.APP_SECRET, redirect_uri=url)
        return WechatUser.api.get_authorize_url(scope=WechatUser.scope)

    def getUserInfo(code):
        auth_info = WechatUser.api.exchange_code_for_access_token(code=code)
        data = WeixinAPI(access_token=auth_info['access_token'])
        return data.user(openid=auth_info['openid'])

    def __init__(self, popenid, pname, pprofile):
        super(WechatUser, self).__init__(pname)
        self.openid = popenid
        self.profile = pprofile

    def add(self):
        query = 'select count(*) from User where third_party_id = "' + str(self.openid) + '";'
        res = self.condb.executeCurFetchOne(query)
        if res[0] > 0:
            return False
        query = 'insert into User (name, profile, third_party_id) values (\'' + self.name + '\', \'' + self.profile + '\', \'' + str(self.openid) + '\');'
        self.condb.commit(query)
        return True

    def getId(popenid):
        query = 'select id from User where third_party_id = \'' + popenid + '\';'
        condb = ConnectionDB()
        res = condb.executeCurDictFetchOne(query)
        return res['id']

    def getJson(self, lang):
        pass
