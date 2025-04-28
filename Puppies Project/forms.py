from flask_wtf import FlaskForm
from wtforms import (StringField,IntegerField,SubmitField)

class AddForm(FlaskForm):

    name = StringField('Name of the Puppy : ')
    submit = SubmitField('Add Puppy')



class DelForm(FlaskForm):
    id = IntegerField('Id number of Puppy to Remove : ')
    submit = SubmitField('Remove Puppy')