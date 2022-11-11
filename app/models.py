"""
Module describe models for ORM and DB
"""
from time import time
from datetime import datetime
from hashlib import md5
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login, app


followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id')))


class User(UserMixin, db.Model):
    """
    Represent User model into DB
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self)->str:
        return f'<User: {self.username}>'

    def set_password(self, password: str)->None:
        """
        Function for set user password
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str)->bool:
        """
        Function for check password
        """
        return check_password_hash(self.password_hash, password)

    def avatar(self, size: int)->str:
        """
        Get user avatar from gravatar
        """
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def follow(self, user):
        """
        Followed current user other user
        """
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        """
        Unfollowed current user other user
        """
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user)->bool:
        """
        Check followed current user other user
        """
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        """
        Create list of posts for own and followed users
        """
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def get_reset_password_token(self, expires_in:int=600)->str:
        """
        Generate jwt token to reset password
        """
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in},
        app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password(token:str):
        """
        Verify token for reset password
        """
        try:
            cur_id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(cur_id)


@login.user_loader
def load_user(cur_id: int):
    """
    Get user id for Flask_login
    """
    return User.query.get(int(cur_id))


class Post(db.Model):

    """
    Represent Post model into DB
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: {self.body}>'
