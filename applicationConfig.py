import os

DEBUG = False

SECRET_KEY = '\xb2\xcd]9\xa6\xad\xaf\xc6\xb1NSz\xdbT\x044\x19\xfac\xf7y\xef\x18\x97'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

del os