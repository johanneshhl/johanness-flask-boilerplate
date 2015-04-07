from application import app
from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/<password>")
def hello(password):
    testString = bcrypt.generate_password_hash(password)
    return testString

@app.route("/")
def hello3():
    return 'hej verden :)'
