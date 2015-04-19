 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.database.database import User
from application.models.user import *
from application.views.decorators.decorators import *
from application.functions.functions import *




"""
UserSite



"""
#	
#@app.route('/session/user/<int:user_id>')
#@login_required
#def userpage(user_id):
#
#	if user_id == 0:	
#		user = g.user
#		user_id = User.query.filter_by(username=user).first().id
#
#	user = User.query.filter_by(id=user_id).first()
#
#	if user != None:
#		return render_template('secret.html', input_var=(user.username + ' - ' + str(user.lastLogin)))
#	else:
#		return render_template('secret.html', input_var='Brugen findes ikke')
#
#

@app.route('/session/user')
@login_required
def userpage():
	
	user = User.query.filter_by(username=g.user).first()
	if user != None:
		return render_template('secret.html', input_var=(user.username + ' - ' + str(user.lastLogin)))
	else:
		return render_template('secret.html', input_var='Brugen findes ikke')
	



#Login system - form input
#				Username 
#				Password
#				KeepMeLoggedIn


@app.route('/session/login', methods=['POST','GET'])
def login():
	

	'''
		Her skal kommentaren stå :)


	'''



	
	if 'next' in request.args:
		returnURL = request.args['next']
	else:
		returnURL = url_for('index')


	if request.method == 'POST' and g.userIsloggedIn == False:
		loggedIn = tryLogin(request.form['username'], request.form['password'], request.form['KeepMeLoggedIn'], request.form['authenticity_token'])
		
		if loggedIn[2] != '':
			flash(loggedIn[1], loggedIn[2])
		else:
			flash(loggedIn[1])


		if loggedIn[0] == False: 

			serverAuthenticationCode = bcrypt.generate_password_hash(app.config['SECRET_KEY'], 2)
			return render_template('login.html', formerUsernameInput=request.form['username'], setAuthenticationCode=serverAuthenticationCode)

		return redirect(returnURL)

	else:
		if 'next' in request.args and g.userIsloggedIn:
			return redirect(request.args['next'])

		elif g.userIsloggedIn:
			flash('Du er allrede logget ind som {}'.format(g.user),'info')
			return redirect(returnURL)

		else:
			serverAuthenticationCode = bcrypt.generate_password_hash(app.config['SECRET_KEY'], 2)
			return render_template('login.html', setAuthenticationCode=serverAuthenticationCode)





@app.route('/session/createuser', methods=['POST','GET'])
def createUser():

	'''
		Her skal kommentaren stå :)


	'''



	serverAuthenticationCode = bcrypt.generate_password_hash(app.config['SECRET_KEY'], 2)
	returnURL = url_for('index')
	
	if (request.method == 'POST') and g.userIsloggedIn == False:
		
		theUser = tryCreateUser(request.form['username'], request.form['password'], request.form['KeepMeLoggedIn'], request.form['authenticity_token'])

		if theUser[2] != '':
			flash(theUser[1], theUser[2])
		else:
			flash(theUser[1])

		if theUser[0] == False: 
			returnURL = url_for('createUser')

		return redirect(returnURL)
	
	else:

		if g.user != None:
			flash('Du er allrede logget ind som {}'.format(g.user),'info')
			return redirect(url_for('index'))
		else:
			serverAuthenticationCode = bcrypt.generate_password_hash(app.config['SECRET_KEY'], 2)
			return render_template('createuser.html', setAuthenticationCode=serverAuthenticationCode)



#Log af bruger system - form input

@app.route('/session/logout')
def logout():

	'''
		Her skal kommentaren stå :)


	'''

	if g.userIsloggedIn != True:
		flash('Du er ikke logget ind', 'info')
		return redirect(url_for('login'))
	else:
		session.pop('username', None)
		session.clear() 
		flash('Du er nu logget ud')
		return redirect(url_for('index'))
