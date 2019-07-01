#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/6/28 14:33
from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
from app import routes
