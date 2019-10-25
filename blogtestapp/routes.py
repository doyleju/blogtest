from blogtestapp import app
from flask import render_template

@app.route('/')
@app.route('/index/')
def index():

    user = { 'username': 'Justin' }
    posts = [ { 'author': { 'username': 'Jack' }, 'body': 'This is Jack\'s comment' }, { 'author': { 'username': 'Simon' }, 'body': 'Simon says ...' } ]

    return render_template('index.html', title='Home', user=user, posts=posts)

