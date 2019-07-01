#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/6/28 17:55

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #定义数据库的路径
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False