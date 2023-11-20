# import smtplib
# import ssl

# SSL - Secure Socket Layer
# 465 - port
# port = 465
# smtplib_server = "smtp.gmail.com"
# from_email = "absaitovdev@gmail.com"
# receiver_email = "absaitovdev@gmail.com"
# password = "okhaexmwdbbcoiab"
# message = "Hello Javohir"
#
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtplib_server, port , context=context) as server:
#     print(server.login(from_email, password))
#     server.sendmail(from_email, receiver_email, message)
#
#
#

import logging



#
#
#
# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# sender_email = "behruztest123@gmail.com"
# receiver_email = "behruztest123@gmail.com"
# password = "ymngkjjrzzqlanee"
#
# message = MIMEMultipart("alternative")
# message["Subject"] = "multipart test"
# message["From"] = sender_email
# message["To"] = receiver_email
#
# text = """\
# Hi,
# How are you?
# Real Python has many great tutorials:
# www.realpython.com"""
#
#
# part1 = MIMEText(text, "plain")
#
# message.attach(part1)
#
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(
#         sender_email, receiver_email, message.as_string()
#     )






logging.basicConfig(filename="TEST.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


import smtplib
import ssl

port = 465
smtplib_server = "smtp.gmail.com"
from_email = "behruztest123@gmail.com"
receiver_email = "behruztest123.com"
password = "ymngkjjrzzqlanee"
message = "Hello"
context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL(smtplib_server,port,context=context) as server:
        print(server.login(from_email, password))
        server.sendmail(from_email,receiver_email,message)
        logging.info("Saqlandi")
except Exception as e:
    logging.warning(f"{e} bu email xato!")





















