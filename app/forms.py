#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/6/28 17:15
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(label=u'用户名', validators=[DataRequired()])
    password = PasswordField(label=u'密码',validators=[DataRequired()])
    remember_me = BooleanField(label=u'忘记密码')
    submit = SubmitField(label=u'登录')


class RegistrationForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired()])
    email = StringField('邮箱地址',validators=[DataRequired(),Email()])
    password = PasswordField('密码',[DataRequired()])
    password2 = PasswordField('重复密码',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('提交注册')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("用户名已存在！")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('该邮箱已被用户注册！')


class EditProfileForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired()])
    about_me = TextAreaField('关于我',validators=[length(min=0,max=140)])
    submit = SubmitField('提交资料')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('请输入正常的用户名')
