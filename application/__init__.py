 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for, session, escape, render_template, g, flash
from flask.ext.heroku import Heroku 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.assets import Environment, Bundle

from datetime import datetime


app = Flask(__name__)
app.config.from_object('applicationConfig')


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
assets = Environment(app)


# Find filer der skal minifierser
js = Bundle('js/jquery.min.js', 'js/main.js', 'js/bootstrap.min.js', filters='jsmin', output='gen/packed.js')
css = Bundle('css/bootstrap.min.css', 'css/style.css', 'css/bootstrap-theme.min.css', output='gen/packed.css')

# Hent de minifiserde filer
assets.register('js_all', js)
assets.register('css_all', css)



from application.functions import *
from application.database import database
from application.views import views



db.create_all()