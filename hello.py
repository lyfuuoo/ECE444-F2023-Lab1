from flask import Flask, render_template, session, redirect, url_for, flash
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError
import re

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'guess key'

class validationEmail(object):
        def __call__(self, form, field):
            email = field.data
            if '@' not in email:
                raise ValidationError(f'Please include an @ in the email. {field.data} is missing an @.')
            
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT email address?', validators=[DataRequired(), validationEmail()])
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
        old_email = session.get('email')
        if old_name and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        if old_email and old_email != form.email.data:
            flash('Looks like you have changed your email!')

        if 'utoronto' in form.email.data:
            session['email'] = form.email.data
        else:
            session['email'] = 'invalid'
        return redirect(url_for('index'))
    return render_template('question.html', form = form, name = session.get('name'), email=session.get('email'))

@app.route('/user/<name>/')
def user(name):
    # return '<h1>Hello, {}!</h1>'.format(name)
    return render_template('user.html',name =name ,current_time=datetime.utcnow())
