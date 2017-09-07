#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-


import sys

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import ioloop, gen
from tornado.options import define, options


sys.path.append('/var/server/beejeen/controller')

from IndexHandler import IndexHandler
from LookHandler import LookHandler
from PageHandler import PageHandler
from SearchHandler import SearchHandler
from CountryHandler import CountryHandler
from CityHandler import CityHandler
from CityItemHandler import CityItemHandler
from TourHandler import TourHandler
from FavorHandler import FavorHandler
from TravelHandler import TravelHandler
from RedirectionHandler import RedirectionHandler
from LoginPageHandler import LoginPageHandler
from LoginHandler import LoginHandler
from POICountryHandler import POICountryHandler
from POICityHandler import POICityHandler
from POIUploadHandler import POIUploadHandler
from POICheckHandler import POICheckHandler
from CommentHandler import CommentHandler
from PMHandler import PMHandler
from RegisterHandler import RegisterHandler
from AddCommentHandler import AddCommentHandler
from GetCommentHandler import GetCommentHandler
from UserLoginHandler import UserLoginHandler
from WechatLoginHandler import WechatLoginHandler
from mWechatLoginHandler import mWechatLoginHandler
from WechatAuthHandler import WechatAuthHandler
from CheckTelephoneHandler import CheckTelephoneHandler
from WeixinCheckHandler import WeixinCheckHandler
from StaticHandler import StaticHandler



application = tornado.web.Application([])


application.settings = {
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "pmlogin": "/bjloginpage",
}

application.add_handlers(r"^(beejeen).*",[
    # () in regex which is matched will be passed to function get/post as parameter
	(r"/(.*)", RedirectionHandler),
])


#application.add_handlers(r"^(www|localhost|172\.*).*",[
application.add_handlers(r"^(www).*",[
	(r"/(.*\.js$)", StaticHandler, {'path': 'beejeen/'}),
	(r"/(.*\.css$)", StaticHandler, {'path': 'beejeen/'}),
	(r"/(.*\.xml$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.jpg$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.png$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.ico$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.gif$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.ttf$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.eof$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.svg$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.txt$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.woff$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(html/pm\.html)", PMHandler),
	#(r"/(aaaaa$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.html$)", StaticHandler, {'path': 'beejeen/'}),

	(r"/(comment)", CommentHandler),

	(r"/(register)", RegisterHandler),
	(r"/(addcomment)", AddCommentHandler),
	(r"/(getcomment)", GetCommentHandler),
	(r"/(checktelephone)", CheckTelephoneHandler),
	(r"/(login)", UserLoginHandler),
	(r"/(wechatlogin)", WechatLoginHandler),
	(r"/(wechatauth)", WechatAuthHandler),

	(r"/(weixinCheck)", WeixinCheckHandler),

	(r"/(index)", SearchHandler),
	(r"/(look)", LookHandler),
	(r"/(country)", CountryHandler),
	(r"/(city)", CityHandler),
	(r"/(cityitem)", CityItemHandler),
	(r"/(tour)", TourHandler),
	(r"/(travel)", TravelHandler),
	(r"/(like)", FavorHandler),
	(r"/(bjloginpage)", LoginPageHandler),
	(r"/(bjlogin)", LoginHandler),
	(r"/(POICountry)", POICountryHandler),
	(r"/(POICity)", POICityHandler),
	(r"/(uploadPOI)", POIUploadHandler),
	(r"/(POICheck)", POICheckHandler),
	(r"/$", IndexHandler),
])


application.add_handlers(r"^(m).*",[
	(r"/(.*\.js$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.xml$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.css$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.jpg$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.png$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.ico$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.gif$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
    (r"/(.*\.ttf$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.eof$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.svg$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.txt$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.woff$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.html$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),

	(r"/(weixinCheck)", WeixinCheckHandler),
	(r"/(wechatlogin)", WechatLoginHandler),

	(r"/(index)", SearchHandler),
	(r"/(look)", LookHandler),
	(r"/(country)", CountryHandler),
	(r"/(city)", CityHandler),
	(r"/(cityitem)", CityItemHandler),
	(r"/(tour)", TourHandler),
	(r"/(travel)", TravelHandler),
	(r"/(like)", FavorHandler),
	(r"/$", IndexHandler),
])

#define("port", default=443, help="run on the given port", type=int)
define("port", default=80, help="run on the given port", type=int)


if __name__ == "__main__":
    args = sys.argv
    args.append("--log_file_prefix=/var/server/beejeen/bj.log")

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application, max_buffer_size = 838860800)
	#http_server = tornado.httpserver.HTTPServer(application, ssl_options={
    #    "certfile": "cert/domain.crt",
    #    "keyfile": "cert/domain.key",
    #})
    http_server.listen(options.port)
    io_loop = tornado.ioloop.IOLoop.instance()
    import tornado.autoreload
    tornado.autoreload.start(io_loop, 1000)
    io_loop.start()

