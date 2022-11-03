import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    FLASK_HOST = str(os.environ.get('flask_host'))
    FLASK_PORT = int(str(os.environ.get('flask_port')))
