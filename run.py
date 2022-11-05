"""
Module for run application
"""
from app import app, db
from app.models import User, Post
print(app.config.get('SQLALCHEMY_DATABASE_URI'))

@app.shell_context_processor
def make_shell_context()->dict:
    """Define initialization of Flask Shell
    """
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == "__main__":
    app.run(host=app.config.get('FLASK_HOST'), port=app.config.get('FLASK_PORT'))
