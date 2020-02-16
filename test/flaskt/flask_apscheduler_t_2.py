from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask import Flask
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


def show_users():
    with db.app.app_context():
        print(User.query.all())


class Config(object):
    JOBS = [
        {
            'id': 'job3',
            'func': show_users,
            'trigger': 'interval',
            'seconds': 2
        }
    ]

    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url='sqlite:///flask_context.db')
    }

    SCHEDULER_API_ENABLED = True


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_context.db'

    db.app = app
    db.init_app(app)

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    app.run()




    def init_db():
        import sqlite3
        conn = sqlite3.connect('flask_context.db')
        cursor = conn.cursor()
        cursor.execute('create table IF NOT EXISTS user (id varchar(20) primary key, username varchar(80), email varchar(120))')
        cursor.execute('insert into user (id, username,email) values (\'2\', \'Michael\', \'Michael@gmail.com\')')
        print(cursor.rowcount)
        cursor.close()
        conn.commit()
        conn.close()

    #init_db()