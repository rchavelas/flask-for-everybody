"""
This is a boilerplate for using the sqlite3 module within flask for opening
a database connection and excecuting commands to the database.

In this app, we store a class instance in the database, which in some
situations might be necessary if the class needs to be permanently
stored and it is too complex to change it to something that an ORM can
understand.

Make sure to open a terminal and run 'python init_db.py' to initialize the 
database before running the application.

"""

from flask import Flask, render_template, request, url_for, redirect
import sqlite3
import pickle 


# Define a function to create a database connection
def get_db_connection():
    conn = sqlite3.connect('items.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_app():
    app = Flask(__name__)
    
    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            conn = get_db_connection()
            item = conn.execute('SELECT * FROM items WHERE id = ?',("1")).fetchone()
            foo_instance = pickle.loads(item["instance"])
            foo_instance.increment()            
            conn.execute("UPDATE items SET instance = ? WHERE id = ?",
                         (sqlite3.Binary(pickle.dumps(foo_instance)),"1"))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))   
        
        conn = get_db_connection()
        item = conn.execute('SELECT * FROM items WHERE id = ?',("1")).fetchone()
        foo_instance = pickle.loads(item["instance"])
        conn.close()

        return render_template('index_with_form.html', instance_attribute=foo_instance.bar)

    return app
