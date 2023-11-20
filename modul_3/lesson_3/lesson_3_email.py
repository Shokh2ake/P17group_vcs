# smtplib , ssl
#behruzpdp@gmail.com
import smtplib
import ssl

# SSL - Secure Socket Layer
# 465 - port
port = 465
smtplib_server = "smtp.gmail.com"
from_email = "shokhake6690@gmail.com"
receiver_email = "najmiddinovavaz22@gmail.com"
password = "dixafrrbylojopnr"
message = "Qandesz Behruz aka darslar yaxshi ketayabdimi?"

context = ssl.create_default_context()
while True:
    with smtplib.SMTP_SSL(smtplib_server, port , context=context) as server:
        print(server.login(from_email, password))
        server.sendmail(from_email, receiver_email, message)



import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "shokhake6690@gmail.com"
receiver_email = "aralovjavoxir@gmail.com"
password = "dixafrrbylojopnr."

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""


part1 = MIMEText(text, "plain")

message.attach(part1)

context = ssl.create_default_context()
while True:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

