#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-

import sys
import os
import tornado.web

import urllib.parse
import tornado.escape

from City import City
from Sight import Sight
from Hotel import Hotel
from Activity import Activity
from Restaurant import Restaurant



class POIUploadHandler(tornado.web.RequestHandler):
    def post(self, path):
        try:
            print('POIUploadHandler')
            print(self.request.uri)
            val = tornado.escape.url_unescape(self.get_argument('type'))
            print(val)
            if val == 'Hotel':
                checkInOut = self.get_body_argument('checkout-in-out')
                prepayment = self.get_body_argument('prepayment')
            else:
                openTime = self.get_body_argument('open-time')
                cost = self.get_body_argument('cost')

            country = self.get_body_argument('country', 'country missing')
            city = self.get_body_argument('city', 'city missing')
            name_en = self.get_body_argument('name-en', 'name-en missing')
            name_cn = self.get_body_argument('name-cn', 'name-cn missing')
            intro_cn = self.get_body_argument('intro-cn', 'intro-cn missing')
            continent = self.get_body_argument('continent', 'continent missing')
            telephone = self.get_body_argument('telephone', 'telephone missing')
            siteweb = self.get_body_argument('siteweb', 'siteweb missing')
            arrivalMode = self.get_body_argument('arrival-mode', 'arrival-mode missing')
            address = self.get_body_argument('address', 'address missing')
            remark_cn = self.get_body_argument('remark-cn', 'remark-cn missing')
            service = self.get_body_argument('service', 'service missing')

            print(country)
            print(city)
            print(name_en)
            print(name_cn)
            print(intro_cn)
            print(continent)
            print(telephone)
            print(siteweb)
            print(arrivalMode)
            print(remark_cn)
            print(service)

            obj = eval(str(val) + '(pname_en = "' + name_en + '", pname_cn = "' + name_cn + '", pintro_cn = "' + intro_cn + '", pcountry = "' + country + '", pcity = "' + city + '")')
            if obj.add() == 0:
                print('insert  fail')
                self.write('1')

            path = 'tmp_Backup ' + country + '/Backup ' + country + '/' + city + '/' + val + 's/' +  name_en + '/'
            os.makedirs(path)
            print('thumb:')
            print(self.request.files['thumb'][0]['filename'])
            f = self.request.files['thumb'][0]['body']
            fileName = 'thumb ' + name_en + '.jpg'
            print(fileName)
            test = open(fileName, 'wb+')
            test.write(f)
            test.close()
            os.rename(fileName, path + fileName)

            if 'music' in self.request.files:
                print('mp3:')
                print(self.request.files['music'][0]['filename'])
                f = self.request.files['music'][0]['body']
                fileName = name_en + '.mp3'
                print(fileName)
                test = open(fileName, 'wb+')
                test.write(f)
                test.close()
                os.rename(fileName, path + fileName)

            print('img:')
            for num in range(0, int(self.get_body_argument('number'))):
                key = str(num + 1)
                print(self.request.files[key][0]['filename'])
                f = self.request.files[key][0]['body']
                fileName = key + ' ' + self.request.files[key][0]['filename']
                test = open(fileName, 'wb+')
                test.write(f)
                test.close()
                os.rename(fileName, path + fileName)

            print('receive done')
            
            os.rename('tmp_Backup ' + country, './media/tmp_Backup ' + country)
            os.rename('./media/tmp_Backup ' + country, './media/Backup ' + country + '_' + continent)

            self.write('0')
            print('===========================================================')
        except Exception as e:
            print('EXCEPTION FROM POIUploadHandler post:')
            print(e)
            self.write('1')
