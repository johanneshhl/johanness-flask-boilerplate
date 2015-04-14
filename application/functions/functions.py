 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from application import app, request, session, redirect, url_for, db, bcrypt, datetime
from application.database.database import User



#needle in haystack
def conatins(input, string):
	if string in input:
		return True
	else:
		return False


def addUserFromString(name, password):
	hashedpassword = bcrypt.generate_password_hash(password, 7)
	theUser = User(name,hashedpassword)
	db.session.add(theUser)
	db.session.commit()


def testLogin(name, inPassword):
	user = User.query.filter_by(username=name).first()
	if user and bcrypt.check_password_hash(user.password, inPassword):		
		user.lastLogin = datetime.utcnow()
		db.session.commit()
		return True
	else:
		return False

#Username submit test
def userNameTest(usernameInput):
	# Tjek om brugernavenet er tomt 
	if usernameInput == '' :
		return [False, 'brugernavenet er tomt']

	#Tjek om brugernavenet indholder mellemrum
	elif conatins(usernameInput,' ') == True:
		return [False,'Brugernavenet må ikke indholde mellemrum']

	#Tjek om brugernavnet er unikt
	elif db.session.query(User).filter_by(username=usernameInput).count() != 0:
		return [False, 'Brugernavenet findes allerede']

	#ellers retuner Sandt 
	else:
		return True
