 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, url_for, db
from flask.ext.bcrypt import Bcrypt
from application.database.database import User



bcrypt = Bcrypt(app)

@app.route("/test/<password>")
def hello5(password):
    theTest = bcrypt.check_password_hash('$2a$12$RWxScyVhbTuhHCCpvQUnpeKS77G/.0sqD702T8RFT2U/WvehNE7Lu',password)
    
    if theTest == True:
        return 'True'
    else:
        return 'False'

@app.route("/ps/<password>")
def hello(password):
    testString = bcrypt.generate_password_hash(password)
    return testString



@app.route("/test")
def hello2():
    return app.config['SQLALCHEMY_DATABASE_URI']
    
@app.route("/")
def hello3():
    return 'hej verden :)'


def addUserFromString(name, password):
	hashedpassword = bcrypt.generate_password_hash(password)
	theUser = User(name,hashedpassword)
	db.session.add(theUser)
	db.session.commit()

def conatins(input, string):
	if string in input:
		return True
	else:
		return False


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


#Lav bruger test
@app.route('/createuser', methods=['POST','GET'])
def creatUser():

	if request.method == 'POST':
		if userNameTest(request.form['username']) == True:
			addUserFromString(request.form['username'],request.form['password'])
			return 'True'
		else:
			return userNameTest(request.form['username'])[1] + ' \n ' + '<form action="" method="post"><p><input type=text name=username><p><input type=password name=password><p><input type=submit value=Login></form>' 

	else:
		return '<form action="" method="post"><p><input type=text name=username><p><input type=password name=password><p><input type=submit value=Login></form>' 



#Login Test koden er = johanneshvilsom

totalyRandomPassword = 'johanneshvilsom'

@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		if bcrypt.check_password_hash(totalyRandomPassword , request.form['username']):
			return 'true'
		else:
			return 'False'
	else:
		return '<form action="" method="post"><p><input type=password name=username><p><input type=submit value=Login></form>'
