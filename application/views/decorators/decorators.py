 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from functools import wraps
from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
    	app.logger.debug(session['username'])
        if session['username']:
            return redirect(url_for('login', next=request.url, _external=True, _scheme='https'))
        return f(*args, **kwargs)
    return decorated_function


