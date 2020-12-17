from __init__ import app

from flask import request
from flask import render_template

from wtforms import Form

class ReusableForm(Form):
    
    @app.route("/rebase", methods=['GET', 'POST'])
    def rebase():
        form = ReusableForm(request.form)
        return render_template('rebase.html', form=form)
