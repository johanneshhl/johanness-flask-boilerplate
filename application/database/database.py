 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from application import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    created = db.Column(db.DateTime)
    lastLogin = db.Column(db.DateTime)


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created = datetime.datetime.now()
        self.lastLogin = self.created

    def __repr__(self):
        return '<User %r>' % self.username



class siteInfo(object):
    siteName = db.Column(db.String(64))
    siteOwner = db.Column(db.String(128))


    def __init__(self, arg):
        self.siteName = siteName
        self.siteOwner = siteOwner

    def __repr__(self):
        return '<siteInfo %r>' % self.siteName
 


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fileName = db.Column(db.String(120))
    fileBlob = db.Column(db.LargeBinary)    
    created = db.Column(db.DateTime)

    def __init__(self, fileName, fileBlob):
        self.fileName = fileName
        self.fileBlob = fileBlob
        self.created = datetime.datetime.now()
    def __repr__(self):
        return '%r' % self.id
