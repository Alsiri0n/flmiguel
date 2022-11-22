"""
Represent contoller class for working with User through REST API
"""
from app.api import bp
from flask import jsonify, request
from app.models import User


@bp.route('/users/<int:id>', methods=["GET"])
def get_user(id:int):
    """
    Return a user
    """
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users', methods=['GET'])
def get_users():
    """
    Return the collection of all users
    """
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@bp.route('/users/<int:id>/followers', methods=['GET'])
def get_followers(id:int):
    """
    Return the followers of this user
    """
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followers, page, per_page, 'api.get_followers', id=id)
    return jsonify(data)


@bp.route('/users/<int:id>/followed', methods=['GET'])
def  get_followed(id:int):
    """
    Return the users this user is following
    """
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followed, page, per_page, 'api.get_followed', id=id)
    return jsonify(data)

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
