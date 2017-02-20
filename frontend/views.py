from flask import render_template, send_from_directory
from frontend import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/publink')
def publink():
    return send_from_directory(app.static_folder, 'publink/index.html')
