 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from application import app, abort, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.database.database import User
from application.models.user import *
from application.views.decorators.decorators import *
from application.functions.functions import *




@app.route('/session/upload')
@login_required
def uploadFile():
	
	return render_template('upload.html')
	
