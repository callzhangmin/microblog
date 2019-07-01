#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/6/28 14:33
from flask import Flask
from config import Config
from  flask_sqlalchemy import SQLAlchemy
from  flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)




from app import routes, models


