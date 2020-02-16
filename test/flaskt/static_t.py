from flask import request
from flask import Flask, escape, url_for,render_template

app = Flask(__name__)

@app.route('/static', methods=['GET', 'POST'])
def get_static():
    return url_for('static', filename='style.css')


@app.route('/show', methods=['GET', 'POST'])
def get_show():
    return render_template('show.html')


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()