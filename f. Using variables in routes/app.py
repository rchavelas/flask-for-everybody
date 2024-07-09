"""
This is a boilerplate for using variables in routes
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

# A route with a string variable
@app.route('/content/<string>')
def content(string):
    return f'This is page for content: {escape(string)}'

# A route with an integer variable
@app.route('/page/<int:page_num>')
def page(page_num):
    return f'This is page #{page_num}'

# A route with a float variable
@app.route('/calc/<float:float_num>')
def calc(float_num):
    return f'Calculation on {float_num}'

# A route with a path as a variable 
# (for example, try localhost:5000/path/dir/a/1)
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

if __name__ == '__main__':
    app.run()
