 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from application import app, abort, request, redirect, escape, session, url_for, db, bcrypt, render_template, g, flash
from application.database.database import User
from application.models.user import *
from application.views.decorators.decorators import *
from application.functions.functions import *
from werkzeug import secure_filename
import os



@app.route('/session/upload', methods=['POST','GET'])
@login_required
def uploadFile():

	if request.method == 'POST':
		file = request.files['file']
		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
			return app.config['UPLOAD_FOLDER']+'/'+filename
	else:
		return render_template('upload.html')
	
