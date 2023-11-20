# import threading
#
# t1 = threading.Thread(target, args)
# t2 = threading.Thread(target, args)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# import time
#
#
# def a():
#     time.sleep(5)
#
# def b():
#     time.sleep(5)
#
# start = time.time()
# # a()
# # b()
#

# import smtplib
# import ssl
# import time
#
# emails = """leetcodemee23@gmail.com
# akbaralisalohiddinov808@gmail.com
# sarvarismatullayev7@gmail.com
# fazliddinismoilov234@gmail.com
# javoxirmamatayev@gmail.com
# aralovjavoxir@gmail.com
# jahonsaitqulov@gmail.com
# fayzullaxojaevi@gmail.com
# azamovshahboz06082001@gmail.com
# dadturchi@gmail.com
# ominanuriddinova2212@gmail.com
# sokidjonovabdulbosit53@gmail.com
# behruzpdp@gmail.com
# akhdeveloper777@gmail.com
# nodirovshoxzod717@gmail.com
# ozodbekyarkinov@gmail.com""".split('\n')
#
#
# def email_():
#     port = 465
#     smtplib_server = "smtp.gmail.com"
#     from_email = "jahonsaitqulov@gmail.com"
#     receiver_email = emails
#     password = "dixafrrbylojopnr"
#     message = "Qandesz aka darslar yaxshi ketayabdimi?"
#
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL(smtplib_server, port , context=context) as server:
#         print(server.login(from_email, password))
#         server.sendmail(from_email, receiver_email, message)
# print(email_())
# print(time.time())


# import multiprocessing
# import os
# import time
#
#
# def a(num):
#     time.sleep(2)
#     print(f"{num} {os.getpid()}")
#
# with multiprocessing.Pool(16) as p:
#     p.map(a, [1, 2, 3, 4, 5, 6, 7, 8])

# P1 = multiprocessing.Process(target=a, args=(2,))
# P2 = multiprocessing.Process(target=a, args=(10,))
#
# P1.start()
# P2.start()
# P1.join()
# P2.join()






