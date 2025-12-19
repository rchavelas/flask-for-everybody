import sqlite3
try:
    conn = sqlite3.connect('items.db')
    print('SQLite connection successfully initialized \n')

    cursor = conn.cursor()
    with open('schema.sql') as f:
        cursor.executescript(f.read())
    cursor.execute("INSERT INTO items (content) VALUES (?)",("1st item",))
    conn.commit()
    cursor.close()

except sqlite3.Error as error:
    print(f'An error occurred - {error}, exception class is:  {error.__class__}')

finally:
    if conn:
        conn.close()
        print('SQLite connection successfully closed')
