#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/6/28 14:37
from app import app,db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm,RegistrationForm,EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime


#一旦某个用户向服务器发送请求，就将当前时间写入到这个字段。
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()

#主页路由
@app.route('/')
@app.route('/index')
@login_required
def index():
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
    return render_template('index.html',title='HELLO',posts=posts)


#登录路由
@app.route('/login', methods=['GET','POST'])
def login():
    #如果已经登录
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('用户名或密码错误，请检查')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html',title='登录',form=form)


#退出登录路由
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#注册路由
@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功！')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#个人主页
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'test1'},
        {'author': user, 'body': 'test2'},
    ]
    return render_template('user.html',user=user,posts=posts)

#个人信息编辑页
@app.route('/edit_profile',methods=['GET','POST'])
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('修改个人信息成功！')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html',title='个人信息',form=form)
