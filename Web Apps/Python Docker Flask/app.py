from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is a Python Flask Application in Docker Container'
