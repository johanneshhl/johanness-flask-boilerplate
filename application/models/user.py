 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from application import Flask, app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.functions.functions import *
from application.database.database import User
import datetime




def tryCreateUser(userName, userPassword, remeberMe, authenticateCode):

	'''
		create User 

	'''

	returnBool = False
	returnString = u''
	returnType = 'error'

	u = userFromUserName(userName)
	secret = bcrypt.check_password_hash(authenticateCode, app.config['SECRET_KEY'])

	if u == False and secret == True and passwordCheck(userPassword) == True:
		hashedpassword = bcrypt.generate_password_hash(userPassword, 7)
		theUser = User(userName,hashedpassword)
		
		db.session.add(theUser)
		db.session.commit()

		loginUser(theUser, remeberMe)

		returnBool = True
		returnString = '{} created!'.format(userName)
		returnType = ''

	else:
		returnBool = False
		returnString = 'Could not create user'
		returnType = 'error'


	return [returnBool, returnString, returnType]



def tryLogin(userName, userPassword, remeberMe, authenticateCode):

	'''
		Prøv at logge ind, og hvis den 

	'''

	returnBool = False
	returnString = u''
	returnType = 'error'

	u = userFromUserName(userName)
	secret = bcrypt.check_password_hash(authenticateCode, app.config['SECRET_KEY'])

	if u and authenticateUser(u, userPassword) and secret:
		loginUser(u, remeberMe)
		returnBool = True
		returnString = 'Logged in as {}!'.format(u.username)
		returnType = ''	
	else: 
		returnBool = False
		returnString = 'Incorrect username or password.'
		returnType = 'error'
	
	return [returnBool, returnString, returnType]










def authenticateUser(userObj, inPassword):
	'''
		Tjek om bruger obj's kodeord = input koden. 

	'''
	if bcrypt.check_password_hash(userObj.password, inPassword):
		return True
	else:
		return False




def loginUser(userObj, rememberMe):

	session.permanent = False
	remeber = False

	userName = userObj.username
	User.query.filter_by(username=userName).first().lastLogin = datetime.datetime.now()
	db.session.commit()

	if rememberMe == 'true':
		remeber = True
		session.permanent = True

	session['username'] = userName
	session['LoggedIn'] = True
	session['remeber_me'] = remeber



