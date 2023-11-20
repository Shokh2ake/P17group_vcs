from modul_4.lesson_4.MonitorAdmin.db import DB

class User(DB):

        def __init__(self, id: int = None,
                     first_name: str = None,
                     last_name: str = None,
                     phone: str = None,
                     birthday: str = None,
                     username: str = None,
                     password: str = None,
                     is_admin: bool = False
                     ):
            self.id = id
            self.first_name = first_name
            self.last_name = last_name
            self.phone = phone
            self.birthday = birthday
            self.username = username
            self.password = password
            self.is_admin = is_admin


        def is_valid(self):
            pass


        def is_login(self):
            query = """
                select * from userssss where username = %s and password = %s
            """
            params = (self.username, self.password)
            self.cur.execute(query, params)
            user = self.cur.fetchone()
            if user :
                return User(*user)
            raise Exception("Not fount accaund")


        def select(self, **kwargs):
            pass

        def insert(self):
            query = """
                insert into userssss(first_name, last_name, phone, birthday, username, password)
                values (%sz, %s, %s, %s, %s, %s)
            """
            p = self.__dict__.copy()
            p.pop("id")
            params = tuple(*p.values())
            self.cur.execute(query, params)
            self.con.commit()



        def update(self):
            pass