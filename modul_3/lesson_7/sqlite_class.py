import datetime
import sqlite3
from abc import ABC, abstractmethod

import asyncio

a
class DB(ABC):
    con = sqlite3.connect("test.sqlite")
    cur = con.cursor()

    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def select(self):
        pass
    @abstractmethod
    def delete(self):
        pass
    @abstractmethod
    def update(self,field, new_val):
        pass

class User(DB):
    def __init__(self,
                 id : int = None,
                 name : str = None,
                 username : str = None,
                 password : str = None,
                 created_at : str = None,
                 updated_at : str = None
                 ):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

    def is_validate(self):
        if len(self.password)< 4:
            raise Exception("Password xato🖕")

    def insert(self):
        try:
            query = """
                insert into users(name , username , password,created_at , update_at)
                values (?,?,?,?,?)
            """
            params = (self.name , self.username , self.password , self.created_at , self.updated_at)
            self.cur.execute(query , params)
            self.con.commit()
        except:
            raise Exception("Username yoki password xato🖕")

    def select(self):
        query = """
            select * from users where username = ? and password = ?;
        """
        params = (self.username , self.password)
        self.cur.execute(query , params)
        user = self.cur.fetchone()
        if user:
            return User(*user)
        return None

    def delete(self):

        query = """
            delete from users where username = ?;
        """
        params = (self.username,)
        self.cur.execute(query , params)
        self.con.commit()

    def update(self,field, new_val):
        query = f"""
            update users set {field} = ? where id = ?;
        """
        params = (new_val , self.id)
        self.cur.execute(query , params)
        self.con.commit()