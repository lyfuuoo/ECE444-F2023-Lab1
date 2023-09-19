from flask import Flask, render_template, session, redirect, url_for, flash
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'guess key'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# index page
# @app.route('/')
@app.route('/', methods=['GET', 'POST'])
def index():
    # activity 2
    # return '<h1>Hello World!</h1>'

    # activity 3
    # return render_template('index.html',current_time=datetime.utcnow())

    # activity 4
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('question.html', form = form, name = session.get('name'))

@app.route('/user/<name>/')
def user(name):
    # return '<h1>Hello, {}!</h1>'.format(name)
    return render_template('user.html',name =name ,current_time=datetime.utcnow())
