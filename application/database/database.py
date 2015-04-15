 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    created = db.Column(db.DateTime)
    lastLogin = db.Column(db.DateTime)


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created = datetime.now()
        self.lastLogin = self.created

    def __repr__(self):
        return '<User %r>' % self.username

