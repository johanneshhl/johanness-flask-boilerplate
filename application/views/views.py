from application import app
from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/test/<password>")
def hello5(password):
    testString = bcrypt.check_password_hash('$2a$12$RWxScyVhbTuhHCCpvQUnpeKS77G/.0sqD702T8RFT2U/WvehNE7Lu',password)
    return testString


@app.route("/<password>")
def hello(password):
    testString = bcrypt.generate_password_hash(password)
    return testString

@app.route("/test")
def hello2():
    return app.config['SQLALCHEMY_DATABASE_URI']
    
@app.route("/")
def hello3():
    return 'hej verden :)'
