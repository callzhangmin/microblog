#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/6/28 14:33
import logging
from flask import Flask
from config import Config
from  flask_sqlalchemy import SQLAlchemy
from  flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
#初始化login
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
#数据库迁移引擎migrate
migrate = Migrate(app, db)

from app import routes, models, errors

if not app.debug:
    if not os.path.exists('logs'):
        os.makedirs('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
