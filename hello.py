from flask import Flask

app = Flask(__name__)

#如果访问根目录‘/’，返回index
@app.route('/')
def index():
    return 'index'

#如果访问目录‘/hello’，返回hello
@app.route('/hello')
def hello():
    return 'hello'