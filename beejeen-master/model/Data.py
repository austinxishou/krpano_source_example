#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

from ConnectionDB import ConnectionDB
import base64


## for POICode
# Country: 1
# City: 2
# Sight: 3
# Hotel: 4
# Activity: 5
# Restaurant: 6


class Data(metaclass=ABCMeta):
    def __init__(self, pname = '', pparamForWechat = '', pname_en = '', pname_cn = '', pintro_cn = '', pcountry = '', pcity = ''):
        self.condb = ConnectionDB()
        self.name = pname
        self.paramForWechat = pparamForWechat
        self.name_en = pname_en
        self.name_cn = pname_cn
        self.intro_cn = pintro_cn
        self.country = pcountry
        self.city = pcity

    def getCountryidAndCityid(self):
        query = 'select id from Country where name_en = \'' + self.country + '\';'
        res = self.condb.executeCurFetchOne(query)
        countryid = res[0]
        query = 'select id from City where name_en = \'' + self.city + '\';'
        res = self.condb.executeCurFetchOne(query)
        cityid = res[0]
        return countryid, cityid

    def convertEOL(self, msg):
        return msg.replace("\r\n", "<br/>").replace("\n", "<br/>")
        #return msg.replace("\"", "\\\"").replace("\r\n", "<br/>").replace("\n", "<br/>")

    def doFavor(self):
        query = 'update ' + self.__class__.__name__ + ' set adore = adore + 1 where name_en = \'' + self.name + '\' or name_cn = \'' + self.name + '\';'
        self.condb.commit(query)

    @abstractmethod
    def getJson(self, lang):
        pass

    def getVersionCode():
        return str(201708283)
