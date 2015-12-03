#*- coding:utf-8 -*-

import os
import tornado
import logging
import hashlib

from tornado.web import (
    RequestHandler,
    Application,
    authenticated,
    StaticFileHandler,
    RedirectHandler,
    authenticated,
)

from tornado.wsgi import WSGIApplication
from tornado.escape import json_decode, json_encode

import re
import tornado.database
import tornado.options
import unicodedata

import _mysql
import datetime
import base64
import uuid

MYSQL_DB = "Experiment"
MYSQL_USER = "root"
MYSQL_PASS = "993613"
MYSQL_HOST_M = "localhost"
MYSQL_HOST_S = ""
MYSQL_PORT = 8080
MYSQL_HOST = "%s:%s" % (MYSQL_HOST_M, str(MYSQL_PORT))

rootdir = os.path.split(unicode(os.path.realpath(__file__),'gb2312'))[0]

settings = {
    "autoreload": True,
    "debug": True,
    "static_path": os.path.join(rootdir,"static"),
    "login_url": "/",
   # "xsrf_cookies": True,
    "cookie_secret":"61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
}

class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("paperTester")

    def initialize(self):
        try:
            self.json = {}
            if self.request.body != "":
                self.json = json_decode(self.request.body)
            self.ret = {}
            self.db = tornado.database.Connection(MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASS, max_idle_time = 5)
        except:
            logging.traceback.print_exc()
            #self.send()

    def send(self, data = {}):
        ret = {}
        ret['data'] = data
        ret['request'] = self.request.body + " " + self.request.uri
        ret = json_encode(ret)
        self.write(ret + "======")
        self.finish()

    def on_finish(self):
        pass

class RegisterHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("./static/index.html")

class RegistHandler(BaseHandler):
    def post(self):
        try:
            self.set_secure_cookie("paperTeste", self.json['Student_ID'])
            self.db.execute("insert into `User` (`Student_ID`,`Name`) values ('%s', '%s')"%(str(self.json['Student_ID']), str(self.json['Name'])))
            self.send({"student_ID": self.json['Student_ID']})
        except:
            logging.traceback.print_exc()

class SAEApplication(tornado.wsgi.WSGIApplication):
    def __init__(self, url, **metadata):
        logging.basicConfig(level=logging.INFO)
        tornado.wsgi.WSGIApplication.__init__(self, url, **metadata)

router = [
        (r"/", RegisterHandler),
        (r"/post/Regist", RegistHandler),
        (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
]
