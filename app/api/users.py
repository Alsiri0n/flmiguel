"""
Represent contoller class for working with User through REST API
"""
from app.api import bp
from flask import jsonify
from app.models import User


@bp.route('/users/<int:id>', methods=["GET"])
def get_user(id:int):
    """
    Return a user
    """
    pass


@bp.route('/users', methods=['GET'])
def get_users():
    """
    Return the collection of all users
    """
    pass


@bp.route('/users/<int:id>/followers', methods=['GET'])
def get_followers(id:int):
    """
    Return the followers of this user
    """
    pass


@bp.route('/users/<int:id>/followed', methods=['GET'])
def  get_followed(id:int):
    """
    Return the users this user is following
    """
    pass

@bp.route('/users', methods=['POST'])
def create_user():
    """
    Register a new user account
    """
    pass


@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """
    Modify a user
    """
    pass
