# -*- coding: UTF-8 -*-
# 当前项目的名称: flask_class 
# 新文件名称：config 
# 当前登录名：LuckyLu
# 创建日期：2020/9/23 13:25
# 文件IDE名称：PyCharm 

import os


class Config:
    SECRET_KEY = os.urandom(32)
    DEBUG = False
    JWT_HEADER_TYPE = 'JWT'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_USER = r"sqlite://LemonPlatform.db"
    JWT_HEADER_TYPE = 'JWT'
    SECRET_KEY = "your secret key"


class ProConfig(Config):
    pass