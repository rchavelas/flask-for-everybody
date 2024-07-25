"""
This is a boilerplate for using the sqlite3 module within flask for opening
a database connection and excecuting commands to the database.

We'll use the sqlite3 module, as it is already available in the standard
Python library

Make sure to open a terminal and run 'python init_db.py' to initialize the 
database before running the application. 

"""

from flask import Flask, render_template, request, url_for, redirect
import sqlite3

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
            content = request.form['content']
            conn = get_db_connection()
            conn.execute("INSERT INTO items (content) VALUES (?)",
                         (content,))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))   
        
        conn = get_db_connection()
        items = conn.execute('SELECT * FROM items').fetchall()
        conn.close()
        return render_template('index_with_form.html', items=items)

    return app
