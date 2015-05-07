 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from application import Flask, app, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.functions.functions import *
from application.database.database import File
import datetime


def tryCreateFile(orgFileName, fileUrl):

	'''
		create New File 

	'''
	theFile = File(orgFileName, fileUrl)
	app.logger.debug(orgFileName + '\n' + fileUrl)
	db.session.add(theFile)
	db.session.commit()
	returnID = File.query.filter(File.filePath.ilike(fileUrl)).first()

	return str(returnID.id)

