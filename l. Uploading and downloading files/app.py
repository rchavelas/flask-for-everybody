"""
This is a boilerplate for uploading and downloading files from a server
using Flask.

You should have an -uploads- folder within the main directory

For a more detailed description and explanations see:
https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/

"""

import os
from flask import Flask, request, redirect, render_template, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename

def create_app():
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = 'uploads'

    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            # 1st validation: check if the post request has the file_name part
            if 'file_name' not in request.files:
                return redirect(url_for('upload_file'))
            file = request.files['file_name']
            # 2nd validation: check if the user uploaded a file
            if file.filename == '':
                return redirect(url_for('upload_file'))
            # Now save the file in the server
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('download_file', name=filename))
        else:
            return render_template('index_with_form.html')
        
    @app.route('/uploads/<name>')
    def download_file(name):
        return send_from_directory(app.config['UPLOAD_FOLDER'], name)

    return app
