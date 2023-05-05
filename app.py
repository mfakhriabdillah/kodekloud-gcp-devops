from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, simple Flask application'


@app.route('/info')
def halo():
    return 'This is an information page'

@app.route('/blog')
def halo():
    return 'This is a blog page'    