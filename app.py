import os

from flask import Flask, flash, render_template, redirect, request
from flask_wtf import Form
from wtforms import Form, IntegerField, RadioField, SelectField, StringField, SubmitField, TextField, TextAreaField, validators, ValidationError

app = Flask(__name__)
app.secret_key = 'development key'


class MondaineForm(Form):
    source = RadioField('Duurzame opwek', choices = [('wind','Wind op land'),('solar','Zonneparken')])
    area_type = RadioField('Gebiedstype', choices = [('gemeenten','Gemeenten'),('provincies','Provincie')])
    area_code = TextField("Gebiedscode",[validators.Required("Vul de gebiedscode in..")])
    submit = SubmitField("Verkennen")


@app.route('/')
def index():
    return 'Mondaine (Proof of Concept)'

@app.route('/opwek', methods=['GET', 'POST'])
def opwek():
    form = MondaineForm()

    # if form.validate_on_submit():
    #     type = form.area_type.data
    #     code = form.area_code.data
    #
    #     os.system('python3 connect_to_etm.py {} {}'.format(type, code)
    #
    #     return render_template('sucess.html')

    if request.method == 'POST' and form.validate():
        # os.system('python3 connect_to_etm.py gemeenten GM0448')
        return render_template('success.html')
    elif request.method == 'GET':
        return render_template('opwek.html', form=form)

@app.route('/warmte')
def built_environment():
    return 'Under construction..'

if __name__ == '__main__':
    app.run(debug = True)
