import sqlite3

connection = sqlite3.connect('items.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO items (content) VALUES (?)",("1st item",))

connection.commit()
connection.close()