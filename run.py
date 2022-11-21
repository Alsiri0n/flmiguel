"""
Module for run application
"""
from app import create_app, db, cli
from app.models import User, Post, Notification, Message, Task


app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context()->dict:
    """Define initialization of Flask Shell
    """
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification,
            'Task': Task}


if __name__ == "__main__":
    app.run(host=app.config.get('FLASK_HOST'), port=app.config.get('FLASK_PORT'))
