from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, HiddenField
from wtforms.validators import InputRequired, NumberRange, ValidationError
from app import db
from app.models import Movie

class RateMovieForm(FlaskForm):
    rating = DecimalField('Rating',
                          validators=[
                              InputRequired(),
                              NumberRange(min=0, max=10, message="Please enter a rating between 0.0 and 10.0")
                          ])
    review = StringField('Review',
                         validators=[
                             InputRequired()
                         ])
    submit = SubmitField("Update Movie")

class AddMovie(FlaskForm):
    title = StringField('Movie Title',
                        validators=[
                            InputRequired()
                        ])
    submit = SubmitField("Add Movie")