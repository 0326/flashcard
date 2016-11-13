#-*- coding: UTF-8 -*-
from flask import Flask
from flaskext.mysql import MySQL
import os, sys

application = Flask(__name__)
mysql = MySQL()

mysql.init_app(application)

@application.route('/')
def hello_world():
    return 'Hello FlashCard+!'

@application.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@application.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        application.debug = True
    application.run()
