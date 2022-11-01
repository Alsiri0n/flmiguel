from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index() -> str:
    user = {'username': 'Alsiri0n'}
    return render_template('index.html', title='Home', user=user)
