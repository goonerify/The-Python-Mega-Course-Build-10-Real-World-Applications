import sqlite3

# Database will be created if it doesn't already exist
conn=sqlite3.connect('lite.db')
cur=conn.cursor()

def drop_table():
    cur.execute('DROP TABLE store')
    conn.commit()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()

def insert_data(item, quantity, price):
    cur.execute('INSERT INTO store (item, quantity, price) VALUES (?,?,?)', (item, quantity, price))
    conn.commit()

def view_data():
    cur.execute('SELECT * FROM store')
    rows=cur.fetchall()
    return rows

def close_connection():
    conn.close()

def main():
    drop_table()
    create_table()
    insert_data("Water Glass", 10, 5)
    insert_data("Coffee Cup", 12, 7)
    print(view_data())
    close_connection()

if __name__=='__main__':
    main()
