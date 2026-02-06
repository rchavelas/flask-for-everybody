import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('users.db')

with open('schema.sql') as f:
    conn.executescript(f.read())
    
cursor = conn.cursor()
cursor.execute('INSERT INTO users (email, password_hash) VALUES (?,?) ', 
    ("usr@mail.com", generate_password_hash("secret"),))

conn.commit()
cursor.close()
conn.close()
