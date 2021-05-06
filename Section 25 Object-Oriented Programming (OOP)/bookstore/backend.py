import sqlite3
from string import Template


class Database:
    def __init__(self) -> None:
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        try:
            self.cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (?,?,?,?)", (title, author, year, isbn))
            self.conn.commit()
            return self.cur.lastrowid
        except sqlite3.OperationalError:
            return None

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self, title = "", author = "", year = "", isbn = ""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

print('My name is {}'.format(__name__))
# print(insert("The North", "John Snow", 0000, 133466778))
# insert("The Earth", "John Smith", 1927, 912709990)
# delete(1)
# update(4, "The Moon", 'John Smooth', 1927, 111111111)
# print(view())
# print(search(author="John Smith"))

