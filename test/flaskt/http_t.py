
from flask import request
from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def show_the_login_form():
    return "<h1>show_the_login_form</h1>"


if __name__ == '__main__':
    app.run()