 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from functools import wraps
from application import Flask, app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.functions.functions import *



def login_required(f):
    @wraps(f)
    
    def decorated_function(*args, **kwargs):
    	app.logger.debug(replaceHTTP(request.url))
        if g.user == None:
            return redirect(url_for('login', next=replaceHTTP(request.url), external=True, scheme="https"))
        return f(*args, **kwargs)
    return decorated_function


