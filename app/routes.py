#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/6/28 14:37
from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'zhangmin'}
    posts = [
        {
            'author': {'username': '张无忌'},
            'body': '倚天屠龙记'
        },
        {
            'author': {'username': '段誉'},
            'body': '天龙八部'
        }
    ]
    return render_template('index.html',title='HELLO',user=user,posts=posts)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for use {}, remember_me={}'.format(
            form.username.data,form.remember_me.data))
        return redirect('index')
    return render_template('login.html',title='登录',form=form)