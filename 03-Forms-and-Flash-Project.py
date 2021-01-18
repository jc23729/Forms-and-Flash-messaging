from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] ='mysecretkey'

class InfoForm(FlaskForm):
  breed = StringField('What breed are you?')
  submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
  form = InfoForm()
  if form.validate_on_submit():
    session['breed'] = form.breed.data
    flask(f" You just changed your breed to:{session['breed']}")
    return redirect(url_for("index"))

return render_template('03-home.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)

