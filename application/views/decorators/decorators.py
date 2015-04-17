 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from functools import wraps
from application import app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function