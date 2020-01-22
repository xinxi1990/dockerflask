#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from flask_script import Manager
from app import app

host = '127.0.0.1'
#host = '192.168.1.112'

manager = Manager(app)
manager.add_command('clean', Clean())
manager.add_command('url', ShowUrls())
manager.add_command('server', Server(host=app.config.get('HOST', host),port=app.config.get('PORT', 5000)))

@manager.command
def deploy():
    """Run deployment tasks."""
    pass


@manager.command
def myprint():
    print('hello world...')


if __name__ == '__main__':
    manager.run()