import sqlite3
# Для работы с foreign key его необходимо включить в соединении с БД - conn.execute("PRAGMA foreign_keys = 1")


def connect():
    conn = sqlite3.connect("warehouse.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Categorys
    (CID INTEGER PRIMARY KEY,
    Category TEXT)
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Goods
    (ID INTEGER PRIMARY KEY,
    Good TEXT,
    Count INT,
    BID INT,
    FOREIGN KEY (BID) REFERENCES CATEGORYS (CID))''')
    conn.commit()
    conn.close()


def insert():
    conn = sqlite3.connect("warehouse.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()

    n = [('Milks',), ('Meats',), ('Breads',), ('Vegetables',), ('Fruits',)]
    cur.executemany('''INSERT INTO Categorys (Category) VALUES (?)''', n)
    conn.commit()

    t = [('Milk-0', 10,  1), ('Milk-1', 12, 1), ('Meat-0', 5, 2), ('Meat-1', 7,  2), ('Meat-2', 9, 2),
         ('Bread-0', 7, 3), ('Bread-1', 12, 3), ('Bread-2', 10, 3), ('Vegetable-0', 20, 4), ('Vegetable-1', 23, 4),
         ('Fruit-0', 16, 5), ('Fruit-1', 18, 5)]
    cur.executemany('''INSERT INTO Goods (Good, Count, BID) VALUES (?, ?, ?)''', t)
    conn.commit()
    conn.close()


def select():
    conn = sqlite3.connect("warehouse.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()

    selects = 'SELECT CID, Category, Good, Count FROM Categorys INNER JOIN Goods ON Categorys.CID = Goods.BID'
    cur.execute(selects)
    result = cur.fetchall()
    for x in result:
        print(x)


if __name__ == '__main__':
    connect()
    insert()
    select()
