from application import app, request, redirect, url_for
from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/test/<password>")
def hello5(password):
    theTest = bcrypt.check_password_hash('$2a$12$RWxScyVhbTuhHCCpvQUnpeKS77G/.0sqD702T8RFT2U/WvehNE7Lu',password)
    
    if theTest == True:
        return 'True'
    else:
        return 'False'

@app.route("/ps/<password>")
def hello(password):
    testString = bcrypt.generate_password_hash(password)
    return testString




@app.route("/test")
def hello2():
    return app.config['SQLALCHEMY_DATABASE_URI']
    
@app.route("/")
def hello3():
    return 'hej verden :)'




#Login Test koden er = johanneshvilsom

totalyRandomPassword = 'johanneshvilsom'

@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		if bcrypt.check_password_hash(totalyRandomPassword , request.form['username']):
			return 'true'
		else:
			return 'False'
	else:
		return '<form action="" method="post"><p><input type=password name=username><p><input type=submit value=Login></form>'
