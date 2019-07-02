#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/7/2 16:04
from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def interbal_error(error):
    db.session.rollback()
    return render_template('500.html'),500