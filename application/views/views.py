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
 	if session['username']:
 		return render_template('main.html', functionName_var='Vis bruger')
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


