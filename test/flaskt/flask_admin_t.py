#encoding=utf-8

import os
from flask import Flask
from flask_admin import Admin, expose, BaseView
from flask_admin import Admin,BaseView,expose,AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.fileadmin import FileAdmin
from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from flask_script import Manager

app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123321@192.168.1.105:8888/testcenter?charset=utf8"
app.config['SECRET_KEY'] = '123456'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = SQLAlchemy(app) #初始化数据库
db.create_all()

# admin = Admin(app, name='Admin', template_mode='bootstrap3')


admin = Admin(
    app,
    index_view=AdminIndexView(
        name='导航栏',
        template='welcome.html',
        url='/admin'
    )
)


def init_db():
    import sqlite3
    conn = sqlite3.connect('admin.sqlite')
    cursor = conn.cursor()
    cursor.execute('create table IF NOT EXISTS user (id INTEGER(11) PRIMARY KEY AUTOINCREMENT , username varchar(80), email varchar(120))')
    #cursor.execute('insert into user (id, username,email) values (\'6\', \'Michael\', \'Michael@gmail.com\')')
    cursor.execute('insert into user (username,email) values (\'Michael\', \'Michael@gmail.com\')')
    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()

init_db()


class MicroBlogModelView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))


class PostView(ModelView):
    page_size = 50  # the number of entries to display on the list view


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username =  db.Column(db.String(10))
    email = db.Column(db.String(10))



class MyView(BaseView):

    #这里类似于app.route()，处理url请求
    @expose('/')
    def index(self):
        return self.render('adminshow.html')



class HomeView(BaseView):

    #这里类似于app.route()，处理url请求
    @expose('/')
    def index(self):
        return self.render('adminshow.html')



# admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
# admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))
# admin.add_view(MyView(name='Hello 3', endpoint='test3', category='Test'))
# admin.add_view(ModelView(User, db.session, name='用户'))












class UserView(ModelView):

    #这三个变量定义管理员是否可以增删改，默认为True

    can_delete = True

    can_edit = True

    can_create = True

    can_view_details = True

    #这里是为了自定义显示的column名字

    column_labels = dict(

    username=u'用户名',

    )

    #如果不想显示某些字段，可以重载这个变量

    column_exclude_list = (

    'password_hash',

    )

    # 只需把自己写的处理模型的视图加进去就行了，category是可选的目录




admin.add_view(UserView(User, db.session, name=u'信息', category=u'用户'))
admin.add_view(FileAdmin(os.path.join(os.getcwd(), 'files'), name='文件'))







host = '127.0.0.1'
#host = '192.168.1.112'
port = 5000

manager = Manager(app)
manager.add_command('clean', Clean())
manager.add_command('url', ShowUrls())


manager.add_command('server', Server(host='127.0.0.1',
                                     port='5000',
                                     use_debugger=True
                                     )
                    )


@manager.command
def deploy():
    """Run deployment tasks."""
    pass


@manager.command
def myprint():
    print('hello world...')


#创建数据库脚本
@manager.command
def create_db():
    db.create_all()



if __name__ == '__main__':
    manager.run()