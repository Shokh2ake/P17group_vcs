import sqlite3

con = sqlite3.connect("test.sqlite")
cur = con.cursor()

query = """
    insert into user(name, username, password)
    values ('Kamol', 'Kamol007', '12345');
"""
poducts_table = """
create table products(
    id integer primary
)
"""


cur.execute(query)
con.commit()

