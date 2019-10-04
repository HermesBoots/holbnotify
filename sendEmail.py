#!/usr/bin/env python3
from holbnotify import Creds
import smtplib

def sendEmail(creds, taskList):
    """Sends an email to a user

    Args:
        creds (Creds): Creds object containing user credentials
    """

    # User credential unpacking
    email = creds.email
    paswd = creds.password
    sender = creds.email
    reciever = creds.email

    # Start and login to server to send email
    server = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    server.starttls()
    server.login(email, paswd)

    # Email message to send
    subject = "{} Tasks Failed".format(len(taskList))
    text = "The checker is now available, and you missed {} tasks\n".format(len(taskList))
    text += '\n'.join(str(i) for i in taskList)
    message = "Subject: {}\n\n{}".format(subject, text)

    # Sends the email and exits the server
    server.sendmail(sender, reciever, message)
    server.quit()
