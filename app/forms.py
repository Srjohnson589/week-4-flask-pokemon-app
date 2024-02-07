from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokemonInput(FlaskForm):
    pokemon = StringField('Pokemon: ', validators=[DataRequired()])
    submit_btn = SubmitField('Submit')