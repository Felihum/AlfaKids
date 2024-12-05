import os, random, string

class Config(object):
    CRSF_ENABLE = True
    SECRET = 'dev'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http//%s/%s' % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/alfaKidsDb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': DevelopmentConfig(),
    'testing': None,
    'production': None
}

app_active = os.getenv('FLASK_ENV', 'development')

#if app_config is None:
#    app_config = 'development'