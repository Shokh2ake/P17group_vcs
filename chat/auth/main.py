import json

class File:
    def __init__(self , filename : str = None):
        self.filename = filename

    def read(self):
        with open(self.filename , "r") as f:
            return json.load(f)

    def write(self , datas : list[dict[str]]):
        with open(self.filename , "w") as f:
            json.dump(datas , f , indent=3)

    def clear(self):
        with open(self.filename , "w") as f:
            json.dump([] , f , indent=3)



class User:
    def __init__(self ,
                 id : str = None,
                 fullname : str = None,
                 username : str = None,
                 password : str = None,
                 messages : dict = dict()):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password
        self.messages = messages
        self.file = File("users.json")

    def new_message_data(self):
        res_message = {}
        for from_user , messages in self.messages.items():
            for message in messages:
                if not message.get("is_read"):
                    res_message[from_user] = res_message.get(from_user , []) + [message]
        return res_message


    def is_valid(self):
        users = self.file.read()
        for user in users:
            if user.get("username") == self.username:
                raise Exception("Already exits username !")

    def check_login(self):
        users = self.file.read()
        for user in users:
            if user.get("username") == self.username and user.get("password") == self.password:
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

    def delete(self):
        users = self.file.read()
        for i, user in enumerate(users):
            if user.get("id") == self.id:
                del users[i]
        self.file.write(users)

    def edit(self , field , new_val):
        users = self.file.read()
        for i, user in enumerate(users):
            if user.get("id") == self.id:
                users[i][field] = new_val
        self.file.write(users)

