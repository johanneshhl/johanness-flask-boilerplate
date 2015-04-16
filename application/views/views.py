 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g
from application.database.database import User
from application.functions.functions import *
import application.views.sessions.sessions

@app.before_request
def before_request():
	g.year = datetime.now().year
	g.siteName = 'Johannes Flask Boilerplate'
	g.baseUrl = url_for('index')


@app.errorhandler(404)
def page_not_found(error):
	return render_template('main.html', input_var=error)


@app.route('/')
def index():
	#cookie login remeber me - 
    return render_template('index.html')


@app.route('/showSession')
def showSession():
 	if session:
 		return render_template('main.html', input_var=session)
 	else:
 		return redirect(url_for('login'))



@app.route('/showUser')
def shwoUser():
 	if session['username']:
 		user = User.query.filter_by(username=session['username']).first()
 		return render_template('main.html', functionName_var='Vis bruger')
 	else:
 		return redirect(url_for('login'))



@app.route("/test")
def hello2():
    return app.config['SQLALCHEMY_DATABASE_URI']




@app.route('/session/login', methods=['POST','GET'])
def login():
	
	if request.method == 'POST' and request.form['username'] and request.form['password'] and ('username' not in session):

		if testLogin(request.form['username'], request.form['password']):
			
			session['username'] = request.form['username']

			if request.form['keepMeLogedIn']:
				session.permanent = True
			else:
				session.permanent = False
			
			return redirect(url_for('index'))

		else: 
			return render_template('login.html')
	else:

		return render_template('login.html')


@app.route('/session/createuser', methods=['POST','GET'])
def creatUser():

	if (request.method == 'POST') and ('username' not in session):
		
		if userNameTest(request.form['username'])[0]:

			addUserFromString(request.form['username'],request.form['password'])

			if request.form['keepMeLogedIn']:
				session.permanent = True
			else:
				session.permanent = False

			session['username'] = request.form['username']

			return redirect(url_for('index'))
		else:
			return render_template('createuser.html', userValidate=userNameTest(request.form['username'])), 401
	else:
		return render_template('createuser.html')



@app.route('/session/logout')
def logout():
	session.pop('username', None)
	session.clear() 
	return redirect(url_for('index'))
