import os

DEBUG = False

SECRET_KEY = '\xb2\xcd]9\xa6\xad\xaf\xc6\xb1NSz\xdbT\x044\x19\xfac\xf7y\xef\x18\x97'


#set up localhost usage
if not os.environ.has_key('DATABASE_URL'):
    os.environ['DATABASE_URL'] = 'postgresql://johanneshvilsom@localhost/johanneshvilsom'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')



del os