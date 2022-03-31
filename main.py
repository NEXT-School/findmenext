from flask import Flask
from home import home_code

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/home')
def home():

    val = home_code()
    return(val)
    