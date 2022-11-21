"""
This module necessary to work with email
"""
from threading import Thread
from flask_mail import Message
from flask import current_app
from app import mail


def send_async_email(app, msg):
    """
    Auxiliary function to send async mail
    """
    with app.app_context():
        mail.send(msg)


def send_email(subject:str, sender:str, recipients:list, text_body:str, html_body:str,
                attachments=None, sync:bool=False)->None:
    """
    Send email
    """
    msg = Message(subject=subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)
    if sync:
        mail.send(msg)
    else:
        Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
