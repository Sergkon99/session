from flask import Flask, session
from functools import wraps
import requests

app = Flask(__name__)
app.secret_key = 'qwerty1234'


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'is_logged' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper


@app.route('/')
def index():
    return 'Index page.'


@app.route('/login/<user>')
def login(user: str) -> str:
    session['is_logged'] = True
    session['user_name'] = user
    return 'Hi, {0}. You are successful logged in.'.format(session['user_name'])


@app.route('/logout')
def logout():
    if 'is_logged' not in session:
        return 'Nobody are logged in now'
    session.pop('is_logged')
    return 'Bye, {0}. You are successful logged out.'.format(
            session.pop('user_name'))


@app.route('/profile')
@check_logged_in
def get_profile():
    return 'Hello, {}'.format(session['user_name'])


if __name__ == '__main__':
    app.run(debug=True)
