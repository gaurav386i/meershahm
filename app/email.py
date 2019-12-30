from threading import Thread
from flask import render_template
from app import app, mail
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    """
    method to send emails to end user
    """
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()

def send_password_reset_email(user):
    """
    method to send password reset email to end user
    """
    token = user.get_reset_password_token()
    send_email('[Meershahm] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                          user=uesr, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
