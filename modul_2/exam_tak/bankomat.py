import json
import random


class File:
    def __init__(self, fayl_nomi: str = None):
        self.fayl_nomi = fayl_nomi

    def read(self):
        with open(self.fayl_nomi, "r") as f:
            return json.load(f)

    def write(self, data: list[dict]):
        with open(self.fayl_nomi, "w") as f:
            json.dump(data, f, indent=3)


class User:
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 passport_id: int = None,
                 password: int = None,
                 card_number: int = None,
                 balans: int = 0
                 ):
        self.id = id
        self.fullname = fullname
        self.passport_id = passport_id
        self.password = password
        self.card_number = card_number
        self.balans = balans

    def register(self):
        file = File("bank.json")
        users = file.read()
        user = self.__dict__
        users.append(user)
        file.write(users)

    def login(self, data):
        self.check_login(data)
        UI().account(data)

    def check_login(self, data):
        file = File("bank.json")
        users = file.read()
        for user in users:
            if user.get("card_number") == data.get("card_number") and user.get("password") == data.get("password"):
                UI().account(data)
        else:
            print("Card number yoki password xato!")
            UI().main()

    def check_passport_id(self, data: dict):
        file = File("bank.json")
        users = file.read()
        for user in users:
            if user.get("passport_id") == data.get("passport_id"):
                print("Bunday passport id mavjud")
                UI().main()

    def random_id(self):
        id = random.randrange(1, 10_000_000)
        return self.check_id(int(id))

    def check_id(self, id: int = None):
        file = File("bank.json")
        users = file.read()
        for user in users:
            if user.get("id") == id:
                self.random_id()
        return id

    def random_card_number(self):
        new_card_number = random.randrange(1, 10_000)
        return self.check_card_number(new_card_number)

    def check_card_number(self, new_card_number: int = None):
        file = File("bank.json")
        users = file.read()
        for user in users:
            if user.get("card_number") == new_card_number:
                self.random_id()
        else:
            return new_card_number

    def login_card_number(self, search_card):
        file = File("bank.json")
        users = file.read()
        for i, user in enumerate(users):
            if user.get("card_number") == search_card:
                return i
        else:
            print("Bunday carta topilmadi")

    def check_balans(self, data, summa):
        file = File("bank.json")
        users = file.read()
        for i, user in enumerate(users):
            if user.get("card_number: ") == data.get("card_number: "):
                if user.get("balans") >= summa:
                    users[i]["balans"] = user.get("balans") - summa
                    file.write(users)
                else:
                    print("Mablagʻ yetarli emas")
                    UI().account(data)


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
                new_card_number = User().random_card_number()

                data = {
                    "id": User().random_id(),
                    "fullname": input("Fullname: "),
                    "passport_id": input("Passport id: "),
                    "password": int(input("Password: ")),
                    "card_number": new_card_number
                }
                User().check_passport_id(data)
                data = User(**data)
                data.register()
                print(f"Sizning card nomeringiz {new_card_number}")
                print("Siz royhatdan otdingiz")
                self.main()

            case "2":
                data = {
                    "card_number": int(input("Card number: ")),
                    "password": int(input("Password: "))
                }
                User().login(data)

            case "3":
                return

    def account(self, data):
        menu = """
        1) Pul o'tkazish
        2) Balans
        3) Chiqish
        >>>"""
        key = input(menu)
        match key:
            case "1":
                search_card = int(input("Card number: "))
                file = File("bank.json")
                index = User().login_card_number(search_card)
                summa = int(input("Summa: "))
                User().check_balans(data, summa)
                users = file.read()
                users[index]["balans"] = users[index]["balans"] + summa
                file.write(users)
                print("Toʻlovingiz uchun raxmat!")
                self.account(data)

            case "2":
                file = File("bank.json")
                users = file.read()
                for user in users:
                    if user.get("card_number") == data.get("card_number"):
                        print(user.get("balans"))
                        return self.account(data)

            case "3":
                self.main()


re = UI()
re.main()
