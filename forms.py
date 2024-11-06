from flask_wtf.form import FlaskForm
from wtforms import DateField, SubmitField,SelectField,StringField,IntegerField
from wtforms.validators import InputRequired, Email,length, NumberRange





class Lekse_form(FlaskForm):
    
    frist=DateField('frist',validators=[InputRequired()])
    fag=SelectField('fag',coerce=str, choices=[('matte'),('Fysikk')])
    oppgave = StringField('oppgave', validators=[InputRequired(),length(max=120)],render_kw={"placeholder": "Oppgave 2 kapitel 3 "})
    

    submit=submit=SubmitField("Submit")