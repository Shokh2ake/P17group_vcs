from modul_4.lesson_4.MonitorAdmin.model import User

class UI:
    def main(self):
        session_user : User | None = None
        menu = """
            1) Register
            2) Login
            3) Exit
            >>>"""
        key = input(menu)
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
                "first_name": input("First name: "),
                "last_name": input("Last name: "),
                "phone": input("Phone number: "),
                "birthday": input("Birthday: "),
                "username": input("Username: "),
                "password": input("Password: ")
            }
            user = User(**user)
            user.is_valid()
            user.insert()
            self.main()


        except Exception as e:
            print(e)
            self.main()


    def login(self):
        try:
            login = {
                "username": input("Username: "),
                "password": input("Password: ")
            }
            user = User(**login)
            user = user.is_login()
            self.session_user = user
            if user.is_admin == False : self.user_menu()
            else: self.admin_menu
            self.user_menu()
        except Exception as e:
            print(e)
            self.main()



    def user_menu(self):
        menu = """
            1) Add course
            2) My course
            3) Logout
            >>>"""

    def admin_menu(self):
        menu = """
            1) Add course
            2) Monitor
            3) Logout
        """

