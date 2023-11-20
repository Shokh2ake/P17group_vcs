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
                 password: int = None
                 ):
        self.fullname = fullname
        self.username = username
        self.password = password

    def register(self, user):
        file = File("user.json")
        users = file.read()
        users.append(user)
        file.write(users)


class UI:

    def check_username(self, user):
        file = File("user.json")
        users = file.read()
        for i in users:
            if user.get("username") == i.get("username"):
                print("Bu username mavjud boshqa qoʻying !")

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
                        "password": input("Password: ")
                    }
                    self.check_username(user)
                    User().register(user)
                    print("Foydalanuvchi yaratildi !")

                case "2":
                    user_log = {
                        "username": input("Username: "),
                        "password": input("Password: ")
                    }

                case "3":
                    return

        except Exception as e:
            print(e)
            self.main()


run = UI()
run.main()
