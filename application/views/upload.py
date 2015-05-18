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




@app.route('/session/upload', methods=['POST','GET'])
@login_required
def uploadFile():

	if request.method == 'POST':
		file = request.files['file']
		app.logger.debug(file)
		if file:

			filename = base64.urlsafe_b64encode(os.urandom(30))
			fileNameBase = file.filename.rsplit('.', 1)[0]
			fileExt = file.filename.rsplit('.', 1)[1]
			newFileName = filename+'.'+fileExt

			if os.path.isfile(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], newFileName)) == True:
				app.logger.debug('fejl')
				filename = base64.urlsafe_b64encode(os.urandom(30))
				fileExt = file.filename.rsplit('.', 1)[1]
				newFileName = filename+'.'+fileExt

			file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], newFileName))

			return tryCreateFile(fileNameBase, (app.config['UPLOAD_FOLDER']+'/'+newFileName))
	else:
		return render_template('upload.html')
	



@app.route('/session/download/<int:fileId>')
@login_required
def downloadFile(fileId):

	file = File.query.filter(File.id.ilike(fileId)).first()

	return send_file(os.path.join(app.root_path, file.filePath), as_attachment=True, attachment_filename=file.fileName.encode("ascii","ignore"), mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')