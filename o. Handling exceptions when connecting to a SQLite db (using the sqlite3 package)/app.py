"""
This is a boilerplate for using the sqlite3 module within flask for opening 
a database connection and executing commands to the database. 

This implementation makes sure to handle exceptions and alert the user
when an error ocurrs

Make sure to open a terminal and run 'python init_db.py' to initialize the 
database before running the application. 
"""

from flask import Flask, render_template, request, url_for, redirect, flash
import sqlite3

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'very secret and long random key'

    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            content = request.form['content']
            # INSERT new item into database 
            try:
                conn = sqlite3.connect('items.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO items (content) VALUES (?)",(content,))
                conn.commit()
                cursor.close()
                flash(f'Data was successfully inserted - {content}')
            except sqlite3.Error as error:
                flash(f'An error occurred - {error}')
                print(f'An error occurred - {error}, exception class is:  {error.__class__}')
            finally:
                if conn:
                    conn.close()

            return redirect(url_for('index'))
        
        items = []
        # SELECT all items from database
        try:
            conn = sqlite3.connect('items.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            items = cursor.execute('SELECT * FROM items').fetchall()
            cursor.close()
        except sqlite3.Error as error:
            flash(f'An error occurred - {error}')
            print(f'An error occurred - {error}, exception class is:  {error.__class__}')
        finally:
            if conn:
                conn.close()

        return render_template('index_with_form.html', items=items)
    
    return app
