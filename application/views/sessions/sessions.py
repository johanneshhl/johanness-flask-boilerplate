 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g
from application.database.database import User
from application.functions.functions import *
import application.views.views






#Lav bruger test
@app.route('/session/createuser', methods=['POST','GET'])
def creatUser():

	if request.method == 'POST':
		if userNameTest(request.form['username']) == True:
			addUserFromString(request.form['username'],request.form['password'])
			session['username'] = request.form['username']
			return redirect(url_for('index'))
		else:
			return render_template('createuser.html', userValidate=userNameTest(request.form['username'])), 401
	else:
		return render_template('createuser.html')




#Login fra bruger test
@app.route('/session/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		if testLogin(request.form['username'], request.form['password']):
			session['username'] = request.form['username']
			session.permanent = False
			return redirect(url_for('index'))
		else:
			return redirect(url_for('login'))
	else:
		return render_template('login.html')



@app.route('/session/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
