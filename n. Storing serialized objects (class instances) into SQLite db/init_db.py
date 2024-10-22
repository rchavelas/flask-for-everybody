import sqlite3
import pickle 
from foo_class import Foo

connection = sqlite3.connect('items.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

foo_instance = Foo()
foo_instance.increment()
pickled_foo_instance = pickle.dumps(foo_instance)

cur.execute("INSERT INTO items (instance) VALUES (?)",
            (sqlite3.Binary(pickled_foo_instance),))

connection.commit()
connection.close()