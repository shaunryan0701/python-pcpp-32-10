import sqlite3

conn = sqlite3.connect('todo.db')
conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    priority INTEGER NOT NULL
);
'''
)

conn.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))
conn.commit()
conn.close()
