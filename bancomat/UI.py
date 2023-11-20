from auth.main import User
import random
import datetime
import smtplib
import ssl
import logging

logging.basicConfig(filename="TEST.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


class Random:
    def random_code(self):
        return str(random.randint(1,10000)).zfill(4)

class UI:
    def check_email(self,user):
        port = 465
        smtplib_server = "smtp.gmail.com"
        from_email = "absaitovdev@gmail.com"
        receiver_email = user.get("email")
        password = "okhaexmwdbbcoiab"
        message = Random().random_code()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtplib_server, port , context=context) as server:
            print(server.login(from_email, password))
            server.sendmail(from_email, receiver_email, message)
            return message

    def check_code(self,code,old_code):
        if code != old_code:
            print("error")




    # def random_card(self):
    #     return f"{(str(random.randit(1,1000))).zfile(4)}"

    def main(self):
        # try:
            menu = """
            1) Register
            2) Login
            3) Exit
            >>>"""
            key = input(menu)
            match key:
                case "1":
                    user = {
                        "id":User().create_id(),
                        "fullname": input("fullname : "),
                        "email":input("email : "),
                        "password":input("password"),
                        "create_at":datetime.datetime.now()
                    }
                    old_code = self.check_email(user)
                    code = input("code !")
                    self.check_code(code,old_code)
                    users = User(**user)
                    users.register()

                case "2":
                    pass
                case "3":
                    return
        # except Exception as e:
        #     logging.warning(e)
        #     print(e)
        #

run = UI()
run.main()