#!/usr/local/bin/python3.5
#-*- coding: UTF-8 -*-


import sys

#import tornado.httpserver
#import tornado.ioloop
import tornado.options
import tornado.web
from tornado import ioloop, gen
from tornado.options import define, options


sys.path.append('/var/server/beejeen/controller')

from IndexHandler import IndexHandler
from PageHandler import PageHandler
from SearchHandler import SearchHandler
from FavorHandler import FavorHandler
#from StaticHandler import StaticHandler

sys.path.append('/var/server/beejeen/model')

import ConnectionDB


ConnectionDB.init()

application = tornado.web.Application([])

application.add_handlers(r"^(www).*",[
	(r"/(.*\.js$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.xml$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.css$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.jpg$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.png$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.ico$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),
	(r"/(.*\.html$)", tornado.web.StaticFileHandler, {'path': 'beejeen/'}),

	#(r"/(.*country\.html$)", PageHandler),
	#(r"/(.*city\.html$)", PageHandler),
	#(r"/(.*look\.html$)", PageHandler),
	#(r"/(.*tour\.html$)", PageHandler),
	#(r"/(.*404\.html$)", PageHandler),

	# 每一个页面都必须跳转
	# ajax发送：www.beejeen.com/index?key=国家名
	(r"/(index)", SearchHandler),
	(r"/(like)", FavorHandler),
	(r"/$", IndexHandler),
])


application.add_handlers(r"^(m).*",[
	(r"/(.*\.js$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.xml$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.css$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.jpg$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.png$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.ico$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),
	(r"/(.*\.html$)", tornado.web.StaticFileHandler, {'path': 'mobile/'}),

	# 每一个页面都必须跳转
	# ajax发送：m.beejeen.com/index?key=国家名
	(r"/(index)", SearchHandler),
	(r"/(like)", FavorHandler),
	(r"/$", IndexHandler),
])

define("port", default=443, help="run on the given port", type=int)
#define("port", default=80, help="run on the given port", type=int)


if __name__ == "__main__":
	args = sys.argv
	args.append("--log_file_prefix=/var/server/beejeen/bj.log")

	tornado.options.parse_command_line()
	#http_server = tornado.httpserver.HTTPServer(application)
	http_server = tornado.httpserver.HTTPServer(application, ssl_options={
            "certfile": "cert/domain.crt",
            "keyfile": "cert/domain.key",
        })
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

	ConnectionDB.close()
