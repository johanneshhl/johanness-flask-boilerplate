 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for
from flask.ext.heroku import Heroku 
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('applicationConfig')
db = SQLAlchemy(app)

from application.database import database
from application.views import views



db.create_all()