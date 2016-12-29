# This is the controller file

#importing
import sqlite3
from flask import Flask
from flask import render_template
from flask import request,session, flash,redirect,url_for,g

DATABASE = 'Blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
#Secret key was obtained using urandom(24)
SECRET_KEY = '0\xc2\x07Z-P\xf4\xfb\xa8F\x8c\xee{e}\xb4\xa6#\xf5\xee;\xcb4p'





app = Flask(__name__)
#grabbing the configuration file by looking at UPPERCASE variable
app.config.from_object(__name__)
app.config['DEBUG'] = True




#connecting to databse
def connect_db():
	return sqlite3.connect(app.config['DATABASE']) 




@app.route('/',methods=['GET','POST'])
def login():
	#return render_template('login.html')
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials !! Please Try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html',error=error)





@app.route('/main')
def main():
	return render_template('main.html')



@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash('You were logged out')
	return redirect(url_for('login'))


'''
with app.test_request_context():
	print(url_for('index'))
	print(url_for('main'))
'''

if __name__ == '__main__':
	app.run()
