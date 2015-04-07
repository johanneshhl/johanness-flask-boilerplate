import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = '\xb2\xcd]9\xa6\xad\xaf\xc6\xb1NSz\xdbT\x044\x19\xfac\xf7y\xef\x18\x97'

#DATABASE_URI = os.environ.get('DATABASE_URL')


#DATABASE_CONNECT_OPTIONS = {}
#ADMINS = frozenset(['http://lucumr.pocoo.org/'])

#WHOOSH_INDEX = os.path.join(_basedir, 'flask-website.whoosh')
#DOCUMENTATION_PATH = os.path.join(_basedir, '../flask/docs/_build/dirhtml')

del os