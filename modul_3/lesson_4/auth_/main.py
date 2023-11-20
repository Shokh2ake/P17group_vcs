import json
# import sys
# sys.path.append("/home/ubuntu/PycharmProjects/p17_group/module_3/lesson_4")
from modul_3.lesson_4.DB.main import File

class User:
    def __init__(self,
                 id: str = None, # unique
                 fullname: str = None,
                 email: str = None, # unique
                 password: str = None,
                 balance: int = None,
                 card_number: int = None, # unique
                 created_at : str = None,
                 updated_at : str = None):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.password = password
        self.balance = balance
        self.card_number = card_number
        self.created_at = created_at
        self.updated_at = updated_at
        self.file = File("users.json")



    def is_valid(self):
        users = self.file.read()
        for user in users:
            if user.get("email") == self.email:
                raise Exception("Already exits email !")
            # if (user.get("fullname").split()) < 2:
            #     raise Exception("Invalid fullname")

    def check_login(self):
        users = self.file.read()
        for user in users:
            if user.get("card_number") == self.card_number and user.get("password") == self.password:
                return User(**user)
        else:
            raise Exception("Not Found account")

    def create_id(self):
        users = self.file.read()
        if not users:
            self.id = 1
        else:
            self.id = users[-1].get("id") + 1

    def save(self):
        users = self.file.read()
        user = self.__dict__.copy()
        del user['file']
        users.append(user)
        self.file.write(users)

    # def delete(self):
    #     users = self.file.read()
    #     for i, user in enumerate(users):
    #         if user.get("id") == self.id:
    #             del users[i]
    #     self.file.write(users)

    # def edit(self, field, new_val):
    #     users = self.file.read()
    #     for i, user in enumerate(users):
    #         if user.get("id") == self.id:
    #             users[i][field] = new_val
    #     self.file.write(users)