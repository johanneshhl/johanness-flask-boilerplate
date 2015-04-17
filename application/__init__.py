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


# log to stderr
import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)



from application.functions import *
from application.database import database
from application.views import views



db.create_all()