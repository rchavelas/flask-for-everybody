"""
This is a boilerplate for a web application in Flask showing how to
retrieve (request) information from forms, deal with GET and POST
requests and flash messages into the session.
"""

from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret and long random key'

# In this case, my_list is just a placeholder for information that 
# should be stored in a database. For simplicity, we use a simple list
# to show how to use forms and GET/POST requests 
my_list = ['1st item', '2nd item']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_item = request.form['new_item']
        my_list.append(new_item)
        flash(f"New item submitted: {new_item}")
        return redirect(url_for('index'))
    
    return render_template('index.html', my_list = my_list)

if __name__ == '__main__':
    app.run()
