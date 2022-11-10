"""
This module necessary to work with email
"""
from threading import Thread
from flask_mail import Message
from flask import render_template
from app import mail, app


def send_async_email(app, msg):
    """
    Auxiliary function to send async mail
    """
    with app.app_context():
        mail.send(msg)


def send_email(subject:str, sender:str, recepients:list, text_body:str, html_body:str)->None:
    """
    Send email
    """
    msg = Message(subject=subject, sender=sender, recipients=recepients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_password_reset_email(user)->None:
    """
    Create message to send
    """
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
    sender = app.config['ADMINS'][0],
    recepients = [user.email],
    text_body = render_template('email/reset_password.txt', user=user, token=token),
    html_body = render_template('email/reset_password.html', user=user, token=token))
