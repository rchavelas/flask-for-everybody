import sqlite3

conn = sqlite3.connect('users.db')

with open('schema.sql') as f:
    conn.executescript(f.read())
    
cursor = conn.cursor()
cursor.execute('INSERT INTO users (email, password) VALUES ("usr@mail.com", "secret") ')

conn.commit()
cursor.close()
conn.close()
