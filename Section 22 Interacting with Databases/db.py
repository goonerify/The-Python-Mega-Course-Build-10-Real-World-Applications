import sqlite3
from string import Template

import psycopg2


class SQLiteDatabase:
    def __init__(self) -> None:
        (self.conn, self.cur) = self.connect_db()
        self.drop_table()
        self.create_table()

    def connect_db(self):
        # Database will be created if it doesn't already exist
        conn=sqlite3.connect('lite.db')
        cur=conn.cursor()
        return (conn, cur)

    def drop_table(self):
        self.cur.execute('DROP TABLE store')
        self.conn.commit()

    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
        self.conn.commit()

    def insert_data(self, item, quantity, price):
        self.cur.execute('INSERT INTO store (item, quantity, price) VALUES (?,?,?)', (item, quantity, price))
        self.conn.commit()

    def view_data(self):
        self.cur.execute('SELECT * FROM store')
        rows=self.cur.fetchall()
        return rows

    def delete_record(self, item):
        self.cur.execute('DELETE FROM store WHERE item=?', (item,))
        self.conn.commit()

    def update_record(self, quantity, price, item):
        self.cur.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (quantity, price, item))
        self.conn.commit()
    
    def close_connection(self):
        self.conn.close()


class PostgreSQLDatabase:
    def __init__(self) -> None:
        (self.conn, self.cur) = self.connect_db()
        self.drop_table()
        self.create_table()

    def connect_db(self):
        # Database will be created if it doesn't already exist
        conn=psycopg2.connect("dbname='lite' user='postgres' password='changeme' port='5432' host='localhost'")
        cur=conn.cursor()
        return (conn, cur)

    def drop_table(self):
        self.cur.execute('DROP TABLE IF EXISTS store')
        self.conn.commit()

    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
        self.conn.commit()

    def insert_data(self, item, quantity, price):
        # WARNING: Prone to SQL injection. Don't use python string substitution to create SQL statements
        # self.cur.execute("INSERT INTO store (item, quantity, price) VALUES ('%s','%s','%s')" % (item, quantity, price))
        # This works
        # self.cur.execute("INSERT INTO store (item, quantity, price) VALUES (%s,%s,%s)", (item, quantity, price))
        # This seems best to prevent SQL injection
        template=Template("INSERT INTO store (item, quantity, price) VALUES ('$item', $quantity, $price)")
        self.cur.execute(template.substitute(item=item, quantity=quantity, price=price))
        self.conn.commit()

    def view_data(self):
        self.cur.execute('SELECT * FROM store')
        rows=self.cur.fetchall()
        return rows

    def delete_record(self, item):
        template=Template("DELETE FROM store WHERE item='$item'")
        self.cur.execute(template.substitute(item=item))
        self.conn.commit()

    def update_record(self, quantity, price, item):
        template=Template("UPDATE store SET quantity=$quantity, price=$price WHERE item='$item'")
        self.cur.execute(template.substitute(item=item, quantity=quantity, price=price))
        self.conn.commit()
    
    def close_connection(self):
        self.conn.close()


def main():
    db=SQLiteDatabase()
    db.drop_table()
    db.create_table()
    db.insert_data("Water Glass", 10, 5)
    db.insert_data("Coffee Cup", 12, 7)
    db.delete_record("Water Glass")
    db.update_record(50, 10, "Coffee Cup")
    print(db.view_data())
    db.close_connection()

    db2=PostgreSQLDatabase()
    db2.drop_table()
    db2.create_table()
    db2.insert_data("Water Glass", 10, 5)
    db2.insert_data("Coffee Cup", 12, 7)
    db2.delete_record("Water Glass")
    db2.update_record(50, 10, "Coffee Cup")
    print(db2.view_data())
    db2.close_connection()

if __name__=='__main__':
    main()
