 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.heroku import Heroku 


app = Flask(__name__)
#app.config.from_object('applicationConfig')
heroku = Heroku(app)

from application.views import views


app.run()
