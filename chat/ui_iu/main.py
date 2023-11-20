import json

class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def write(self, data: list[dict]):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=3)


class User:
    def __init__(self, fullname: str = None,
                 username: str = None,
                 password: str = None,
                 come_time=None,
                 back_time=None):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.come_time = come_time
        self.back_time = back_time

    def register(self, user):
        file = File("users1.json")
        users = file.read()
        users.append(user)
        file.write(users)


import time


class UI:
    def logout(self, user_login):
        new_time = str(time.strftime("%Y-%m-%d %H:%M"))
        file = File("users1.json")
        users = file.read()
        for i, user in enumerate(users):
            if user.get("username") == user_login.get("username") and user.get("password") == user_login.get(
                    "password"):
                print(type(str(time.strftime("%Y-%m-%d %H:%M"))))
                users[i]["back_time"] = new_time
                file.write(users)
                run.main()

    def check_login(self, user_login):
        new_time = str(time.strftime("%Y-%m-%d %H:%M"))
        file = File("users1.json")
        users = file.read()
        for i, user in enumerate(users):
            if user.get("username") == user_login.get("username") and user.get("password") == user_login.get(
                    "password"):
                print(type(str(time.strftime("%Y-%m-%d %H:%M"))))
                users[i]["come_time"] = new_time
                users[i]["back_time"] = None
                file.write(users)
                self.acount(user_login)

    def check_username(self, user):
        file = File("users1.json")
        users = file.read()
        for old_user in users:
            if user.get("username") == old_user.get("username"):
                raise Exception("Bunday username bor boshqa qoying !")

    def acount(self, user_login):
        menu = """
        0) Logaut
        >>"""
        key = input(menu)
        match key:
            case "0":
                self.logout(user_login)

    def main(self):
        try:
            menu = """
            1) Register
            2) Login
            3) Exit
            >>>"""
            key = input(menu)
            match key:
                case "1":
                    user = {
                        "fullname": input("Fullname: "),
                        "username": input("Username: "),
                        "password": input("Password: "),
                        "come_time": None,
                        "back_time": None
                    }
                    self.check_username(user)
                    User().register(user)
                    print("Create user")
                    run.main()
                case "2":
                    user_login = {
                        "username": input("Username :"),
                        "password": input("Password")
                    }
                    self.check_login(user_login)
                case "3":
                    return
        except Exception as e:
            print(e)
            self.main()


run = UI()
run.main()