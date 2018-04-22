
# coding:utf-8
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    return "<h1>Hola Mundo Cruel!</h1>"

if __name__ == "__main__":
    app.run()