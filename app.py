# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from flask import Flask, render_template, request

import logging
from logging import Formatter, FileHandler

from forms import (
    SeedForm,
    RegisterForm,
    LoginForm,
    ForgotForm,
)

from untrusted import untrusted

app = Flask(__name__)
app.config.from_object('config')

# Login required decorator.
# def login_required(test):
#     @wraps(test)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return test(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('login'))
#     return wrap


# @app.route('/')
# def home():
#     return render_template('pages/home.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SeedForm(request.form)
    if request.method == 'GET':
        return render_template('forms/seed.html', form=form)

    return untrusted(form.seed.data)


# @app.route('/.well-known/acme-challenge/<_content>')
# def acme_challenge(_content):
#     return 'lmUcOkeLlPM9oTQjVZPxAr6z-k9QNTqOUeiSXErtO6c.fQqRAuyzPCr0VNaJE2k7nzI4zN7bFmWZUg5qvBvOe94'  # noqa
#
#
# @app.route('/about')
# def about():
#     return render_template('pages/about.html')
#
#
# @app.route('/login')
# def login():
#     form = LoginForm(request.form)
#     return render_template('forms/login.html', form=form)
#
#
# @app.route('/register')
# def register():
#     form = RegisterForm(request.form)
#     return render_template('forms/register.html', form=form)
#
#
# @app.route('/forgot')
# def forgot():
#     form = ForgotForm(request.form)
#     return render_template('forms/forgot.html', form=form)


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


if __name__ == '__main__':
    app.run()
    # port = int(os.environ.get('PORT', 5000))
