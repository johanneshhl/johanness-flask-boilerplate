 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from application import app, request, session, redirect, url_for, db, bcrypt, datetime
from application.database.database import User


#needle in haystack
def conatins(input, string):
	if string in input:
		return True
	else:
		return False






def replaceHTTP(url):	
	if conatins(url, app.config['PREFERRED_URL_SCHEME']):
		return url
	else:
		newUrl = url.replace('http', app.config['PREFERRED_URL_SCHEME'])
		return newUrl





def passwordCheck(password):
	'''


	'''


	if password == '' :
		returnBool = False

	elif len(password) < 6:
		returnBool = False

	else:
		returnBool = True

	return returnBool



def userFromUserName(userInput):
	'''
	Get user from input

	'''
	
	u = User.query.filter_by(username=userInput).first()
	
	if u is not None:
		return u
	else:
		return False























# login test
def loginTest(name, inPassword):

	returnBool = False
	returnString = u''

	#Først Tjek username
	user = User.query.filter_by(username=name).first()



	if user == None:
		returnBool = False
		returnString = u'Brugernavenet findes ikke'
	
	elif len(inPassword) <= 1:
		returnBool = False
		returnString = u'Kodeordet er tomt'

	elif bcrypt.check_password_hash(user.password, inPassword) != True:
		returnBool = False
		returnString = u'Kodeordet er forkert'

	else:
		user.lastLogin = datetime.now()
		db.session.commit()
		returnBool = True
		returnString = u'None'

	return [returnBool, returnString]
	


#Username & password submit test
def userTest(usernameInput, passwordInput):
	returnBool = False
	returnString = u''

	#Først tjeck Username

	# Tjek om brugernavenet er tomt 
	if usernameInput == '' :
		returnBool = False
		returnString = u'Brugernavenet er tomt'

	#Tjek om brugernavenet indholder mellemrum
	elif conatins(usernameInput,' ') == True:
		returnBool = False
		returnString = u'Brugernavenet må ikke indholde mellemrum'

	#Tjek om brugernavnet er unikt
	elif db.session.query(User).filter_by(username=usernameInput).count() != 0:
		returnBool = False
		returnString = u'Brugernavenet findes allerede'

	#så Tjeck passwordet
	elif passwordInput == '' :
		returnBool = False
		returnString = u'Kodeordet er tomt'

	elif len(passwordInput) < 6 :
		returnBool = False
		returnString = u'Kodeordet er for kort'

	#ellers retuner Sandt 
	else:
		returnBool = True
		returnString = u'None'


	return [returnBool, returnString]
