# This is the controller file

#importing
import sqlite3
from flask import Flask
from flask import renderer_template
from flask import request,session, flash,redirect,url_for,g

DATABASE = 'Blog.db'
app = Flask(__name__)

#grabbing the configuration file by looking at UPPERCASE variable
app.config.from_object(__name__)
app.config['DEBUG'] = True
#connecting to databse
def connect_db():
	return sqlite3.connect(app.config['DATABASE']) 


@app.route('/')
def login():
	return renderer_template('login.html')

@app.route('/main')
def main():
	return renderer_template('main.html')


if __name__ == '__main__':
	app.run()
