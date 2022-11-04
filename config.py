import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    FLASK_HOST = os.environ.get('flask_host')
    FLASK_PORT = int(os.environ.get('flask_port'))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
        # or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
