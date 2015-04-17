import os
import datetime

if 'DYNO' not in os.environ:
	DEBUG = True
	PREFERRED_URL_SCHEME = 'http'
	PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=365)
	SESSION_COOKIE_PATH = '/'
	SESSION_COOKIE_DOMAIN = '0.0.0.0'
else:

	SESSION_COOKIE_PATH = '/'
	SERVER_NAME = 'jhvilsom.dk'
	SESSION_COOKIE_DOMAIN = '.jhvilsom.dk'
	SESSION_COOKIE_SECURE = True
	SESSION_COOKIE_NAME = 'herokuSession'
	PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=365)
	PREFERRED_URL_SCHEME = 'https'
	DEBUG = False

SECRET_KEY = '\xb2\xcd]9\xa6\xad\xaf\xc6\xb1NSz\xdbT\x044\x19\xfac\xf7y\xef\x18\x97'

#set up localhost usage
if not os.environ.has_key('DATABASE_URL'):
    os.environ['DATABASE_URL'] = 'sqlite:///../test.db'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


del datetime
del os