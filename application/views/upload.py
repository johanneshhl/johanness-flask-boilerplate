 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from application import app, send_file, abort, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.models.file import *
from application.database.database import File
from application.views.decorators.decorators import *
from application.functions.functions import *
from werkzeug import secure_filename
import os
import base64
import io
import StringIO


@app.route('/session/upload', methods=['POST','GET'])
@login_required
def uploadFile():
	
	if request.method == 'POST':
		file = request.files['file']
		if file:
			fileId = tryCreateFile(file.filename, file.read())
			return fileId
	else:
		return render_template('upload.html')
	



@app.route('/session/download/<int:fileId>')
@login_required
def downloadFile(fileId):

	file = File.query.filter(File.id.ilike(fileId)).first()
	strIO = StringIO.StringIO()
	strIO.write(file.fileBlob)
	strIO.seek(0)
	return send_file(strIO, as_attachment=True, attachment_filename=file.fileName.encode("ascii","ignore"), mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')



@app.route('/session/download_raw/<int:fileId>')
def downloadFile2(fileId):

	file = File.query.filter(File.id.ilike(fileId)).first()
	return file.fileName + '\n' + str(file.created)
	#return file.fileBlob