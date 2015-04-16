 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.database.database import User
from application.functions.functions import *

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
















#Login system - form input
#				Username 
#				Password
#				KeepMeLoggedIn


@app.route('/session/login', methods=['POST','GET'])
def login():
	
	if request.method == 'POST' and request.form and ('username' not in session):
		theLoginTest = loginTest(request.form['username'],request.form['password'])

		if theLoginTest[0] == True:
			session['username'] = request.form['username']

			if request.form['KeepMeLoggedIn'] < 1:
				session.permanent = False
			else:
				session.permanent = True

			flash('Vellkommen {}'.format(session['username']))
			return redirect(url_for('index'))

		else: 
			flash(theLoginTest[1], 'error')
			return render_template('login.html')
	else:
		if 'username' in session:
			flash('Du er allrede logget ind som {}'.format(session['username']),'info')
			return redirect(url_for('index'))
		else:
			return render_template('login.html')






#Opret bruger system - form input
#				Username 
#				Password
#				KeepMeLoggedIn


@app.route('/session/createuser', methods=['POST','GET'])
def creatUser():

	if (request.method == 'POST') and ('username' not in session):
		
		if userTest(request.form['username'],request.form['password'])[0] == True:
			addUserFromString(request.form['username'],request.form['password'])
			session['username'] = request.form['username']

			if request.form['KeepMeLoggedIn'] < 1:
				session.permanent = False
			else:
				session.permanent = True
			flash('Vellkommen {}'.format(session['username']))
			return redirect(url_for('index'))

		else:
			flash(userTest(request.form['username'],request.form['password'])[1],'error')
			return render_template('createuser.html'), 401
	else:
		if 'username' in session:
			flash('Du er allrede logget ind som {}'.format(session['username']),'info')
			return redirect(url_for('index'))
		else:
			return render_template('createuser.html')



#Log af bruger system - form input

@app.route('/session/logout')
def logout():
	if ('username' not in session):
		flash('Du er ikke logget ind', 'info')
		return redirect(url_for('login'))
	else:
		session.pop('username', None)
		session.clear() 
		flash('Du er nu logget ud')
		return redirect(url_for('index'))
