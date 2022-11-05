"""
Module for routing into application
"""
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    """
    Create index page of site
    """
    user = {'username': 'Alsiri0n'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in World!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Function for login page
    """
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
