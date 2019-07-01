#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/7/1 13:11
from app import db
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)