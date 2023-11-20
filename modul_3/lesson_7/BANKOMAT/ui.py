import datetime

from main import User




class UI:
    def main(self):
        manu = """
            1) Register
            2) Login
            3) Exit
            >>>"""

        key = input(manu)

        match key:

            case "1":
                self.register()

            case "2":
                self.login()

            case "3":
                return

    def register(self):
        try:
            user = {
                "name": input("Name: "),
                "username": input("Username: "),
                "password": input("Pssword: "),
                "created_at": datetime.date.today(),
                "updated_at": datetime.datetime.now()
            }
            User(**user).insert()
            user
            self.main()
        except Exception as e:
            print(e)
            self.main()