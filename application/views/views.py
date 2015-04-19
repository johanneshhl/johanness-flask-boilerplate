 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.database.database import User
from application.views.user import *
from application.views.decorators.decorators import *
from application.functions.functions import *
from functools import wraps


@app.before_request
def before_request():
	g.year = datetime.now().year
	g.siteName = 'Johannes\' Flask Boilerplate'
	g.baseUrl = url_for('index')

	if 'username' in session:
		user = session['username']
	else:
		user = None

	if 'LoggedIn' in session:
		g.userIsloggedIn = True
	else:
		g.userIsloggedIn = False

	g.user = user


	

@app.errorhandler(404)
def page_not_found(error):
	return render_template('index.html', input_var=error)
 

@app.route('/')
def index():
	#cookie login remeber me - 
    return render_template('index.html')




@app.route('/secret')
@login_required
def denHemmligeSide():
	return render_template('secret.html', input_var=session)