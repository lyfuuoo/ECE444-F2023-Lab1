from flask import Flask, render_template
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# index page
@app.route('/')
def index():
    # return '<h1>Hello World!</h1>'
    return render_template('index.html',current_time=datetime.utcnow())

@app.route('/user/<name>/')
def user(name):
    # return '<h1>Hello, {}!</h1>'.format(name)
    return render_template('user.html',name =name ,current_time=datetime.utcnow())
