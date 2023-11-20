import smtplib, ssl
from email.mime.text import MIMEText

from modul_3.lesson_4.bankomat import UI


def send_email():
    sender_email = "shokhake6690@gmail.com"
    receiver_email = "aralovjavoxir@gmail.com"
    password = "dixafrrbylojopnr."

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    code =
    text = """\
    Hi,
    approve code: {}"""

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    context = ssl.create_default_context()
    while True:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )