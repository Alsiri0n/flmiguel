"""
Module describe models for ORM and DB
"""
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login


class User(UserMixin, db.Model):
    """Represent User model into DB
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self)->str:
        return f'<User: {self.username}>'

    def set_password(self, password: str)->None:
        """Function for set user password
        """
        self.password_hash = generate_password_hash(password)


    def check_password(self, password: str)->bool:
        """Function for check password
        """
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id: int):
    """Get user id for Flask_login
    """
    return User.query.get(int(id))


class Post(db.Model):
    """Represent Post model into DB
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: {self.body}>'
