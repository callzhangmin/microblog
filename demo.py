#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangmin on 2019/7/2 18:20
import zhenzismsclient as smsclient
clent = smsclient.ZhenziSmsClient('https://sms_developer.zhenzikj.com','101966','c65ff2de-a8e5-4204-8b48-3f1309a3ddec')
phonenumber = [15088748900,15397399245]
count = 0
for number in phonenumber:
    result = clent.send(number,'测试我的短信')
    count += 1
print("一共发送了%d条短信"%count)
