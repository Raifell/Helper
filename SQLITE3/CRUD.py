import sqlite3

# Подключение\Создание таблицы, если таблицы нет

conn = sqlite3.connect('example.sql')

cursor = conn.cursor()
create = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY autoincrement, name VARCHAR(50), pass VARCHAR(50));'
cursor.execute(create)
conn.commit()

# Добавление данные в таблицу, через неизвестные значения

insert = 'INSERT INTO users (name, pass) VALUES (?, ?);'
values = [('name-1', 'pass-1'), ('name-2', 'pass-2'), ('name-3', 'pass-3')]

cursor.executemany(insert, values)
conn.commit()

# Выборка данных через .fetchall()

# select = 'SELECT * FROM users;'
# cursor.execute(select)
# results = cursor.fetchall()
#
# print(results)

# Выборка данных через цикл

for x in cursor.execute('SELECT * FROM users;'):
    print(x)

# Обновление данных в таблице (Новое значение, где id = ?)

update = 'UPDATE users SET pass = ? WHERE id = ?;'
cursor.execute(update, ('pass-5', 3))
conn.commit()

for x in cursor.execute('SELECT * FROM users;'):
    print(x)

# Удаление данных из таблицы (где id = ?)

delete = 'DELETE FROM users WHERE id = ?;'
cursor.execute(delete, (2,))
conn.commit()

for x in cursor.execute('SELECT * FROM users;'):
    print(x)

# Закрытие соединения и курсора, после всех действий

cursor.close()
conn.close()
