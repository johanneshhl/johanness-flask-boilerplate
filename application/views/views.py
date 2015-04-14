 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, escape, session, url_for, db, bcrypt
from application.database.database import User
from application.functions.functions import *


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.errorhandler(404)
def page_not_found(error):
	return error

@app.route('/showUser')
def shwoUser():
 	if session['username']:
 		user = User.query.filter_by(username=session['username']).first()
 		return user.username + '\n' + user.password
 	else:
 		return redirect(url_for('login'))






#Lav bruger test
@app.route('/session/createuser', methods=['POST','GET'])
def creatUser():

	if request.method == 'POST':
		if userNameTest(request.form['username']) == True:
			addUserFromString(request.form['username'],request.form['password'])
			session['username'] = request.form['username']
			return redirect(url_for('index'))
		else:
			return userNameTest(request.form['username'])[1] + ' \n ' + '<form action="" method="post"><p><input type=text name=username><p><input type=password name=password><p><input type=submit value=Login></form>' 
	else:
		return '<form action="" method="post"><p><input type=text name=username><p><input type=password name=password><p><input type=submit value="Sign up"></form>' 



#Login fra bruger test
@app.route('/session/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		if testLogin(request.form['username'], request.form['password']):
			session['username'] = request.form['username']
			return redirect(url_for('index'))
		else:
			return redirect(url_for('login'))
	else:
		return '<form action="" method="post"><p><input type=text name=username><p><input type=password name=password><p><input type=submit value=Login></form>' 




@app.route('/session/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
