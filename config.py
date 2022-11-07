"""
This module create all engine for application
"""
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Class for configure applictaion
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    FLASK_HOST = os.environ.get('flask_host')
    FLASK_PORT = os.environ.get('flask_port')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL') \
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT') or 465)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['ADMIN_MAIL']
