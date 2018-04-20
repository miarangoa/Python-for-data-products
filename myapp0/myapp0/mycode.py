from myapp0 import app

@app.route('/')
@app.route('/index')
def index():
    return "Mi primera aplicación en Flask!"