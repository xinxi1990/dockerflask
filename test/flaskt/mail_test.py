#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.mail import Mail, Message
import os

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.126.com',
    MAIL_PROT=25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'autotestin@126.com',
    MAIL_PASSWORD = 'xxxx',
    MAIL_DEBUG = True

)

mail = Mail(app)

@app.route('/')
def index():
    print("准备发送邮件")
# sender 发送方哈，recipients 邮件接收方列表
    msg = Message("Hi!This is a test ",sender='autotestin@126.com', recipients=['xxxx@163.com'])
# msg.body 邮件正文
    msg.body = "This is a first email"
# msg.attach 邮件附件添加
# msg.attach("文件名", "类型", 读取文件）
    with app.open_resource("/Users/xinxi/Documents/sndd/dockerflask/images/flask-debug-tools.jpg") as fp:
        msg.attach("image.jpg", "image/jpg", fp.read())
    mail.send(msg)
    print("Mail sent")
    return "Sent"

if __name__ == "__main__":
    app.run()