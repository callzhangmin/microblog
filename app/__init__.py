#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/6/28 14:33
from flask import Flask
from config import Config
from  flask_sqlalchemy import SQLAlchemy
from  flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
#初始化login
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
#数据库迁移引擎migrate
migrate = Migrate(app, db)

from app import routes, models


