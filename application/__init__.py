 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for, session, escape, render_template, g, flash
from flask.ext.heroku import Heroku 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from datetime import datetime


app = Flask(__name__)
app.config.from_object('applicationConfig')


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application.functions import *
from application.database import database
from application.views import views



db.create_all()