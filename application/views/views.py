 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g
from application.database.database import User
from application.functions.functions import *


@app.before_request
def before_request():
	g.year = datetime.now().year
	g.siteName = 'Johannes Flask Boilerplate'



@app.route('/')
def index():
	#cookie login remeber me - 
    if 'username' in session:
        return render_template('main.html', input_var=('Logged in as %s' % escape(session['username']))) 
    return render_template('main.html', input_var='You are not logged in')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('main.html', input_var=error)




@app.route('/showUser')
def shwoUser():
 	if session['username']:
 		user = User.query.filter_by(username=session['username']).first()
 		return render_template('main.html', input_var=(user.username + '\n' + user.password))
 	else:
 		return redirect(url_for('login'))



@app.route("/test")
def hello2():
    return app.config['SQLALCHEMY_DATABASE_URI']




#Lav bruger test
@app.route('/session/createuser', methods=['POST','GET'])
def creatUser():

	if request.method == 'POST':
		if userNameTest(request.form['username']) == True:
			addUserFromString(request.form['username'],request.form['password'])
			session['username'] = request.form['username']
			return redirect(url_for('index'))
		else:
			return render_template('main.html', input_var=(userNameTest(request.form['username'])[1] + ' \n ' + '<form action="%s" method="post"><p><input type=text name=username><p><input type=password name=password><p><input type=submit value=Login></form>' % url_for('createUser')))
	else:
		return render_template('main.html', input_var=('<form action="" method="post"><p><input type=text name=username><p><input type=password name=password><p><input type=submit value=Login></form>'))



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
		return render_template('main.html', input_var=('<form action="%s" method="post"><p><input type=text name=username><p><input type=password name=password><p><input type=submit value=Login></form>' % url_for('login')))




@app.route('/session/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
