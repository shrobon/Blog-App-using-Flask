# This is the controller file

#importing
import sqlite3
from flask import Flask
from flask import render_template
from flask import request,session, flash,redirect,url_for,g
from functools import wraps

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
	#in-first request nothing will be passed in (i.e it will be GET !!! so no form fill and direct display)
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials !! Please Try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('main')) ## Logged-IN - first page 
	

	return render_template('login.html',error=error) ## passing the error variable for flashing it 


def login_required(test):
	@wraps(test)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return test(*args,**kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap 


@app.route('/main')
@login_required # This decorator has been added to stop unauthenticated login
def main():
	g.db = connect_db()
	cur = g.db.execute('select * from posts')
	posts = [dict(title=row[0],post=row[1])for row in cur.fetchall()]
	g.db.close()
	return render_template('main.html', posts = posts)



@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash('You were logged out')
	return redirect(url_for('login'))






@app.route('/add', methods=['POST'])
@login_required
def add():
	title = request.form['title']
	post = request.form['post']
	if not title or not post:
		flash('All fields are required. Please try again ! ')
		return redirect(url_for('main'))
	else:
		 g.db = connect_db()
		 g.db.execute('insert into posts (title,post) values(?,?)',[request.form['title'],request.form['post']]) 
		 g.db.commit()
		 g.db.close()

		 flash('New entry was successfully posted !')
		 return redirect(url_for('main'))


'''
with app.test_request_context():
	print(url_for('index'))
	print(url_for('main'))
'''

if __name__ == '__main__':
	app.run()
