from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User
from app.api.errors import error_response


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username:str, password:str):
    """
    Realize basic auth for getting token
    """
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


@basic_auth.error_handler
def basic_auth_error(status):
    """
    Return correct error for user
    """
    return error_response(status)


@token_auth.verify_token
def verify_token(token):
    """
    Function for verifying token
    """
    return User.check_token(token) if token else None


@token_auth.error_handler
def token_auth_error(status):
    """
    Return correct error for user
    """
    return error_response(status)
