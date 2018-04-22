
# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def myprog():
    
    ## hace los computos requeridos
    x = np.linspace(0, 2*3.1416, 50, endpoint=True)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, color ='blue');
    plt.xlabel('x');
    plt.ylabel('Sin(x)');
    plt.savefig('examples-08-flask/myApp-04/static/sin.png')

    plt.clf();
    plt.plot(x, y2, color = 'red');
    plt.xlabel('x');
    plt.ylabel('Cos(x)');
    plt.savefig('examples-08-flask/myApp-04/static/cos.png');
    plt.close()
    
    myvar = 18
    
    return render_template('index.html', myvar = myvar)

if __name__ == "__main__":
    app.run()