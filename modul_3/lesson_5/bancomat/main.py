import json
import random
# import datetime
import ssl
import smtplib


class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def write(self, data):
        info = self.read()
        info.append(data)
        with open(self.filename, "w") as f:
            json.dump(info, f, indent=3)


class Random_:
    def id_random_code(self):
        return f"{str(random.randint(1, 1000)).zfill(3)}"

    def card_number_code(self):
        cod = ["8600", "9860", "6262", "5440"]
        return f"{random.choice(cod)} {str(random.randint(1, 10000)).zfill(4)}"

    def email_code(self):
        return f"{str(random.randint(1, 1000)).zfill(2)}"

    def send_email(self, data):
        port = 465
        smtplib_server = "smtp.gmail.com"
        from_email = "shokhake6690@gmail.com"
        receiver_email = data
        password = "dixafrrbylojopnr"
        message = self.email_code()

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtplib_server, port, context=context) as server:
            print(server.login(from_email, password))
            server.sendmail(from_email, receiver_email, message)
        return message


class User:
    def __init__(self,
                 id: str = None,
                 fullname: str = None,
                 card_number: str = None,
                 balance: str = 100_000,
                 email: str = None,
                 password: str = None,
                 # creat_at: str = None,

                 ):
        self.id = id
        self.fullname = fullname
        self.card_number = card_number
        self.balance = balance
        self.email = email
        self.password = password
        # self.creat_at: creat_at

    def register(self):
        user = {
            "id": Random_().id_random_code(),
            "fullname": input("Fullname: "),
            "card_number": Random_().card_number_code(),
            "balance": self.balance,
            "email": input("Email: "),
            "password": input("Password: "),
            # "creat_at": datetime.datetime.now()
        }
        a = Random_().send_email(user.get("email"))
        code = input("Emailingizga yuborilgan codni kiriting: ")

        users = File("user.json")
        if a != code:
            print("Bu cod xato !")
            return
        users.write(user)
        print("Siz muofiqiyatli ro'yxatdan o'tdingiz")

    def login(self):
        user = {
            "fullname": input("Fullname: "),
            "password": input("Password: ")
        }
        users = File("user.json")
        for i in users.read():
            if i["fullname"] == user["fullname"] and i["password"] == user["password"]:
                print("Siz login qildizngiz !")
                return
        print("Bunday foydalanuvchi mavjud emas !")


class UI:
    def main(self):
        menu = """
        1) Register
        2) Login
        3) Exit
        >>>"""
        key = input(menu)

        match key:
            case "1":
                User().register()
                self.main()

            case "2":
                User().login()

            case "3":
                print("Bankomatdan foydalanganingiz uchun raxmat !")
                return


re = UI()
re.main()
