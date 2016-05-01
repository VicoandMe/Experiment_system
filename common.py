#- coding:utf-8 -*-

import os
import time
import random
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
MYSQL_PASS = "123456"
MYSQL_HOST_M = "localhost"
MYSQL_HOST_S = ""
MYSQL_PORT = 8080
MYSQL_HOST = "%s:%s" % (MYSQL_HOST_M, str(MYSQL_PORT))

try:
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT
    MYSQL_HOST = "%s:%s" % (MYSQL_HOST_M, str(MYSQL_PORT))
except:
    pass

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
            print self.json
            self.ret = {}

            self.db = tornado.database.Connection(MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_PASS, max_idle_time = 5)
            testInfo = self.db.query("select * from `TestInfo`") 
            if testInfo != []:
                self.set_secure_cookie("Image_count", testInfo[0]["ImageCountGroup"], expires_days=None)
                self.set_secure_cookie("Question_count", testInfo[0]["QuestionCount"], expires_days=None)
                self.G = ["0"]
                for i in range(1, int(testInfo[0]["ImageCountGroup"]) + 1):
                    index = i
                    str1 = "0"
                    for j in range(0, int(testInfo[0]["ImageCount"])):
                        str1 += str(index)
                        index += 1
                        if index == int(testInfo[0]["ImageCountGroup"]) + 1:
                            index = 1
                    self.G.append(str1)
                print self.G

        except:
            logging.traceback.print_exc()
            print "DB connect error"
    
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
    #@tornado.web.asynchronous
    def get(self):
        self.render("./static/index.html")

class AdminHandler(BaseHandler):
    #@tornado.web.asynchronous
    def get(self):
        self.render("./static/AdminLogin.html")

class RegistHandler(BaseHandler):
    #@tornado.web.asynchronous
    def post(self):
        try:
            self.set_secure_cookie("paperTester", self.json['Student_ID'], expires_days=None)
            self.set_secure_cookie("current_image", "1",  expires_days=None)
            self.set_secure_cookie("current_question", "0", expires_days=None) 
            self.set_secure_cookie("Group_ID", self.json['Group_ID'],  expires_days=None)
            self.db.execute("insert into `User` (`Student_ID`,`Name`) values ('%s', '%s')"%(str(self.json['Student_ID']), str(self.json['Name'])))
            self.send({"student_ID": self.json['Student_ID'], "status" : "200"})
        except:
            logging.traceback.print_exc()
            self.send({"status":"500"});

class ExperimentHandler(BaseHandler):
    #@tornado.web.asynchronous
    def get(self):
        try:
            user = self.get_current_user()
            self.render("./static/Experiment.html", User = user)
        except:
            self.redirect('/', permanent = True)

class GradeHandler(BaseHandler):
    #@tornado.web.asynchronous
    def post(self):
        try:
            value = self.json['value']
            Student_ID = self.get_current_user()
            current_image = self.get_secure_cookie("current_image")
            Image = current_image + '-' + self.G[int(self.get_secure_cookie("Group_ID"))][int(current_image)]
            try:
                self.db.execute("insert into `ImageGrade` (`Image_ID`, `Student_ID`, `Grade`) values ('%s', '%s', '%s')" % (Image, Student_ID, value))
            except:
                self.db.execute("UPDATE `ImageGrade` SET Grade = '%s' WHERE Student_ID = '%s' and Image_ID = '%s'" % (value, Student_ID, Image))
            self.send({"status":"200"})
        except:
            self.send({"status":"500"})

class AnswerHandler(BaseHandler):
    #@tornado.web.asynchronous
    def post(self):
        try:
            current_image = self.get_secure_cookie("current_image")
            image = current_image + '-' + self.G[int(self.get_secure_cookie("Group_ID"))][int(current_image)]
            Q_ID = self.get_secure_cookie("current_question")
            Student_ID = self.get_current_user()
            Answer = self.json["value"]
            print Student_ID, " ", image, " ", Q_ID, " ", Answer
            self.db.execute("insert into `ParticipateAnswer` (`Student_ID`, `Image_ID`, `Q_ID`, `Answer`) values ('%s', '%s', '%s', '%s')" % (str(Student_ID), str(image), str(Q_ID), str(Answer)))
            self.send({"status":"200"})
        except:
            logging.traceback.print_exc()
            self.send({"status":"500"});
           

class AcquireMessageHandler(BaseHandler):
    #@tornado.web.asynchronous
    def post(self):
        try:
            current_image = self.get_secure_cookie("current_image")
            current_question = self.get_secure_cookie("current_question")
            Image = current_image + '-' + self.G[int(self.get_secure_cookie("Group_ID"))][int(current_image)]
            testInfo = self.db.query("select * from `TestInfo`")
            if current_image == "1" and current_question == "0":
                self.set_secure_cookie("startTime", str(int(time.time())),  expires_days=None)
            if int(current_question) >= int(self.get_secure_cookie("Question_count")):
                Student_ID = self.get_current_user()
                useTime = str(int(time.time()) - int(self.get_secure_cookie("startTime")))
                self.set_secure_cookie("startTime", str(int(time.time())),  expires_days=None)
                self.db.execute("insert into `UseTime` (`Student_ID`, `Image_ID`, `UseTime`) values ('%s', '%s', '%s')" % (Student_ID, Image, useTime))
                current_image = str(int(current_image) + 1)
                self.set_secure_cookie("current_image", current_image,  expires_days=None)
                current_question = self.set_secure_cookie("current_question", "0",  expires_days=None)
                current_question = "0"

            if int(current_image) > int(self.get_secure_cookie("Image_count")):
                self.send({"is_End": "1"})
            else:
                current_question = str(int(current_question) + 1)
                self.set_secure_cookie("current_question", current_question)
                Question_Data = self.db.query('select * from Question where Image_ID = \"%s\" and Q_ID = \"%s\"' % (current_image, current_question))
                data = {}
                data["Question"] = Question_Data[0]["Question"]
                data["SelectA"] = Question_Data[0]["SelectA"]
                data["SelectB"] = Question_Data[0]["SelectB"]
                data["SelectC"] = Question_Data[0]["SelectC"]
                data["SelectD"] = Question_Data[0]["SelectD"]
                data["is_End"] = "0"
                if current_question == testInfo[0]["QuestionCount"]:
                    data["sevenPoint"] = "1"
                else:
                    data["sevenPoint"] = "0"
                image = current_image + '-' + self.G[int(self.get_secure_cookie("Group_ID"))][int(current_image)]
                data["image"] = image
                data["sevenPointQuestion"] = testInfo[0]["SevenPointQuestion"]
                data["imageURL"] = testInfo[0]["ImageURL"]
                self.send(data)
        except:
            logging.traceback.print_exc()
            self.send({"status":"500", "is_End":"0"})

class AdminCheckHandler(BaseHandler):
    #@tornado.web.asynchronous
    def post(self):
        try:
            user = self.json["user"]
            password = self.json["password"]
            check_password = self.db.query('select * from Admin where AdminName = \"%s\"' % (str(user)))
            if password == check_password[0]["AdminPassword"]:
                time.sleep(5)
                self.set_secure_cookie("isAdmin", "True", expires_days=None)
                self.send({"status":"200"}) 
            else:
                self.send({"status":"500"})
        except:
            logging.traceback.print_exc()
            self.send({"status":"500"})

class UpdateSettings(BaseHandler):
    #@tornado.web.asynchronous
    def post(self):
        try:
            if self.get_secure_cookie("isAdmin") == "True":
                imageCount = self.json["imageCount"]
                imageCountEach = self.json["imageCountEach"]
                questionCount = self.json["questionCount"]
                sevenPointQuestion = self.json["sevenPointQuestion"]
                imageURL = self.json["imageURL"]
                self.db.execute("delete from `TestInfo`")
                self.db.execute("insert into `TestInfo`(`ImageCount`,`ImageCountGroup`,`QuestionCount`,`SevenPointQuestion`,`ImageURL`) values ('%s', '%s', '%s', '%s', '%s')" % (imageCount, imageCountEach, questionCount, sevenPointQuestion, imageURL))
                self.send({"status":"200"})
        except:
            logging.traceback.print_exc()
            self.send({"status":"500"})

class lnQuestion(BaseHandler):
    #@tornado.web.asynchronous
    def post(self):
        try:
            testInfo = self.db.query("select * from `TestInfo`")
            self.json["questionId"] = self.json["questionId"].split(":")[1]
            questionId = self.json["questionId"]
            (imageId, questionId) = questionId.split("-")
            if self.json["command"] == "next":
                if imageId != testInfo[0]["ImageCount"] or questionId != str(int(testInfo[0]["QuestionCount"])):
                    questionId = str(int(questionId) + 1) 
                    if questionId == str(int(testInfo[0]["QuestionCount"]) + 1):
                        questionId = "1"
                        imageId = str(int(imageId) + 1)
            elif self.json["command"] == "last":
                if  self.json["questionId"] != "1-1":
                    questionId = str(int(questionId) - 1)
                    if questionId == "0":
                        questionId = testInfo[0]["QuestionCount"]
                        imageId = str(int(imageId) - 1)
            questionId = imageId + "-" + questionId
            self.send({"status":"200", "is_End": "0", "questionId": questionId})
        except:
            logging.traceback.print_exc()
            self.send({"status":"500"})

class UploadQuestions(BaseHandler):
    #@tornado.web.asynchronous
    def post(self):
        try:
            self.json["questionId"] = self.json["questionId"].split(":")[1]
            questionId = self.json["questionId"]
            (imageId, questionId) = questionId.split("-")
            question = self.json["question"]
            answerA = self.json["answerA"]
            answerB = self.json["answerB"]
            answerC = self.json["answerC"]
            answerD = self.json["answerD"]
            correctAnswer = self.json["correctAnswer"]
            try:
                self.db.execute("insert into `Question` (`Image_ID` ,\
                        `Q_ID`, `Question`, `SelectA`, `SelectB`, `SelectC`, `SelectD`, `CorrectAnswer`)\
                        values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (imageId, questionId,\
                        question, answerA, answerB, answerC, answerD, correctAnswer))
            except:
                self.db.execute("delete from `Question` where `Image_ID` = '%s' AND `Q_ID` = '%s'" % (imageId, questionId))
                self.db.execute("insert into `Question` (`Image_ID` ,\
                        `Q_ID`, `Question`, `SelectA`, `SelectB`, `SelectC`, `SelectD`, `CorrectAnswer`)\
                        values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (imageId, questionId,\
                        question, answerA, answerB, answerC, answerD, correctAnswer))
            testInfo = self.db.query("select * from `TestInfo`")
            if imageId == testInfo[0]["ImageCount"] and questionId == str(int(testInfo[0]["QuestionCount"])):
                self.send({"status":"200", "is_End": "1"})
                return

            questionId = str(int(questionId) + 1) 
            if questionId == str(int(testInfo[0]["QuestionCount"]) + 1):
                questionId = "1"
                imageId = str(int(imageId) + 1)
            questionId = imageId + "-" + questionId
            self.send({"status":"200", "is_End": "0", "questionId": questionId})
        except:
            logging.traceback.print_exc()
            self.send({"status":"500"})

class SAEApplication(tornado.wsgi.WSGIApplication):
    def __init__(self, url, **metadata):
        logging.basicConfig(level=logging.INFO)
        tornado.wsgi.WSGIApplication.__init__(self, url, **metadata)

router = [
        (r"/", RegisterHandler),
        (r"/Admin", AdminHandler),
        (r"/post/Regist", RegistHandler),
        (r"/post/Experiment", ExperimentHandler),
        (r"/post/Answer", AnswerHandler),
        (r"/post/Grade", GradeHandler),
        (r"/post/AcquireMessage", AcquireMessageHandler),
        (r"/post/Admin", AdminCheckHandler),
        (r"/post/UpdateSettings", UpdateSettings),
        (r"/post/UploadQuestions", UploadQuestions),
        (r"/post/lnQuestion", lnQuestion),
        (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
]
