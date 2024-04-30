import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM tasks'):
    print(row)
conn.close()