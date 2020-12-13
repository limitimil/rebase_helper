from __init__ import app

from flask import request
from flask import flash
from flask import render_template

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

@app.route('/formpoc', methods=['GET'])
def formpoc():
    return 'formpoc', 200

@app.route('/helloviews', methods=['GET'])
def helloviews():
    return 'helloviews', 200

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print( form.errors)
        if request.method == 'POST':
            name=request.form['name']
            print( name)
    
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')
    
        return render_template('hello.html', form=form)
