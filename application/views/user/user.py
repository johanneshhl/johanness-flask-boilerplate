 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.database.database import User
from application.views.decorators.decorators import *
from application.functions.functions import *




"""
UserSite



"""

@app.route('/session/user/', defaults={'user_id': 0})
@app.route('/session/user/<int:user_id>')
@login_required
def userpage(user_id):

	if user_id == 0:	
		user = g.user
		user_id = User.query.filter_by(username=user).first().id

	user = User.query.filter_by(id=user_id).first()

	if user != None:
		return user.username + ' - ' + str(user.lastLogin)
	else:
		return 'Brugen findes ikke'




#Login system - form input
#				Username 
#				Password
#				KeepMeLoggedIn


@app.route('/session/login', methods=['POST','GET'])
def login():
	
	"""Hvis http metoden er post og brugeren ikke er logget ind"""
	if request.method == 'POST' and request.form and g.user == None:
		theLoginTest = loginTest(request.form['username'],request.form['password'])

		if theLoginTest[0] == True:

			"""Hvis loggin virkede lave en session, med brugernavnet"""
			session['username'] = request.form['username']
			g.user = session['username']

			"""Set cookie til permanent hvis bruger har trykket KeepMeLoggedIn"""
			setSessionPermanent(request.form['KeepMeLoggedIn'])

			"""Lav Flash velkomst"""
			flash('Vellkommen {}'.format(session['username']))
			


			"""Brug next url'en hvis brugeren kommer fra en @login_required"""
			if 'next' in request.args:
				return redirect(request.args['next'])
			else:
				"""Gå til forsiden"""		
				return redirect(url_for('index'))

		else: 

			"""Hvis fejl i førsøget på at logge ind, vise fejl og prøv igen"""
			flash(theLoginTest[1], 'error')
			return render_template('login.html')
	else:
		if g.user != None:
			flash('Du er allrede logget ind som {}'.format(g.user),'info')
			return redirect(url_for('index'))
		else:
			return render_template('login.html')







#Opret bruger system - form input
#				Username 
#				Password
#				KeepMeLoggedIn


@app.route('/session/createuser', methods=['POST','GET'])
def creatUser():

	if (request.method == 'POST') and g.user == None:
		
		if userTest(request.form['username'],request.form['password'])[0] == True:
			addUserFromString(request.form['username'],request.form['password'])
			session['username'] = request.form['username']
			g.user = session['username']

			"""Set cookie til permanent hvis bruger har trykket KeepMeLoggedIn"""
			setSessionPermanent(request.form['KeepMeLoggedIn'])


			"""Lav Flash velkomst"""
			flash('Vellkommen {}'.format(session['username']))
			
			"""Gå til forsiden"""		
			return redirect(url_for('index'))


		else:
			flash(userTest(request.form['username'],request.form['password'])[1],'error')
			return render_template('createuser.html'), 401
	
	else:
		if g.user != None:
			flash('Du er allrede logget ind som {}'.format(g.user),'info')
			return redirect(url_for('index'))
		else:
			return render_template('createuser.html')



#Log af bruger system - form input

@app.route('/session/logout')
def logout():
	if g.user == None:
		flash('Du er ikke logget ind', 'info')
		return redirect(url_for('login'))
	else:
		session.pop('username', None)
		session.clear() 
		flash('Du er nu logget ud')
		return redirect(url_for('index'))
