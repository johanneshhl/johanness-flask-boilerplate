from application import app
from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/<password>")
def hello(password):
    testString = bcrypt.generate_password_hash(password)
    return testString

@app.route("/test")
def hello2():
    return app.config['SQLALCHEMY_DATABASE_URI']    
    
    
# Check that an unencrypted password matches one that has
# previously been hashed
