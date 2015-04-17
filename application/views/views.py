 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.database.database import User
from application.views.user.user import *
from application.views.decorators.decorators import *
from application.functions.functions import *

@app.before_request
def before_request():
	g.year = datetime.now().year
	g.siteName = 'Johannes Flask Boilerplate'
	g.baseUrl = url_for('index')
	
	if 'username' not in session:
		g.user = None
	else:
		g.user = session['username']


@app.errorhandler(404)
def page_not_found(error):
	return render_template('main.html', input_var=error)
 

@app.route('/')
def index():
	#cookie login remeber me - 
    return render_template('index.html')




@app.route('/secret')
@login_required
def denHemmligeSide():
	return g.user