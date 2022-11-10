"""
This module necessary to work with email
"""

from flask_mail import Message
from flask import render_template
from app import mail, app


def send_email(subject:str, sender:str, recepients:list, text_body:str, html_body:str):
    """
    Send email
    """
    msg =Message(subject=subject, sender=sender, recipients=recepients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
    sender = app.config['ADMINS'][0],
    recepients = [user.email],
    text_body = render_template('email/reset_password.txt', user=user, token=token),
    html_body = render_tempate('emeil/reset_password.html', user=user, token=token))
