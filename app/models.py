#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/7/1 13:11
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login
class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
#因为数据库对Flask-Login透明，所以需要应用来辅助加载用户。 基于此，插件期望应用配置一个用户加载函数，可以调用该函数来加载给定ID的用户.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140),index=True,default=datetime.utcnow)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)