from bancomat.file_saqlash.main import File


class User:
    def __init__(self,
                 id :str =None,
                 fullname :str = None,
                 email:str = None,
                 password:str = None,
                 card_number:str = None,
                 balance:int = 10_000,
                 create_at :str =None,
                 update_at :str= None
                 ):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.password = password
        self.card_number =card_number
        self.balance = balance
        self.create_at = create_at
        self.update_at = update_at
        self.file = File("users.json")

    def register(self):
        users = self.file.read()
        user = self.__dict__.copy()
        del user["file"]
        users.append(user)
        self.file.write(users)


    def login(self):
        pass

    def update(self):
        pass

    def create_id(self):
        users = self.file.read()
        if not users:
            self.id = 1
        else:
            self.id = users[-1].get("id") + 1