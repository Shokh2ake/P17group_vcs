from chat.auth.main import User
from chat.massage.main import Message

session: User = None

class UI:
    def main(self):
        try:
            menu = """
            1) Register 
            2) Login
            3) Exit
            >>>"""
            key = input(menu)
            match key:
                case "1" :
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except Exception as e:
            print(e)
            self.main()
    def register(self):
        user = {
            "fullname" : input("Fullname :"),
            "username" : input("Username :"),
            "password" : input("Password :"),
        }
        user = User(**user)
        user.is_valid()
        user.create_id()
        user.save()
        print("Success create account !")
        self.main()


    def account(self):
        global session
        messages = session.new_message_data()
        print(messages)
        menu = f"""
        1) Contact
        2) Settings
        3) Message +{len(messages)}
        4) log out
        >>>"""
        key = input(menu)
        match key:
            case "1":
                pass
            case "2":
                pass
            case "3":
                self.messages(messages)
            case "4":
                session = None
                self.main()

    def messages(self , session_messages):
        index = 1
        for username , messages in session_messages.items():
            print(f"{index}) {username} +{len(messages)}")
        print("0) <-back")
        message_index = int(input(">>>"))
        if message_index == 0:
            self.account()
        for i in list(session_messages.values())[message_index - 1]:
            print(" "*10 + i.get('datetime'))
            print(i.get("message"))

        is_answer = input("Javob berasanmi Y/n")
        if is_answer == "n":
            self.account()
        answer_message = input(">>>")
        to_user = list(session_messages.keys())[message_index - 1]
        Message(session.username , to_user,answer_message).add()
        self.account()







    def login(self):
        global session
        user = {
            "username" : input("Username : "),
            "password" : input("Password : ")
        }

        user = User(**user)
        session = user.check_login()
        self.account()




    def chat(self):
        pass

UI().main()