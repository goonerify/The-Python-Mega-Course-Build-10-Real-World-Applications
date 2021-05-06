import sqlite3
from string import Template


def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (?,?,?,?)", (title, author, year, isbn))
        conn.commit()
        return cur.lastrowid
    except sqlite3.OperationalError:
        return None

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title = "", author = "", year = "", isbn = ""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
# print(insert("The North", "John Snow", 0000, 133466778))
# insert("The Earth", "John Smith", 1927, 912709990)
# delete(1)
# update(4, "The Moon", 'John Smooth', 1927, 111111111)
# print(view())
# print(search(author="John Smith"))

