from app import app
from flask import render_template

@app.route('/')
def index():
    print('index')
    return render_template('index.html')

