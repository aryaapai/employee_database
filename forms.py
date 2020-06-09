from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Optional, NumberRange

class InputEmployeeForm(FlaskForm):

    name = StringField('Employee Name', validators=[DataRequired()])
    designation = SelectField('Designation', [DataRequired()],
    choices=[('CEO','CEO'),('Assistant','Assistant' ),('Manager','Manager')])
    address = TextAreaField('Address')
    phone = IntegerField('Phone', validators=[Optional(),
    NumberRange(min=1000000000,max=9999999999,message="Invalid mobile number")])
    email = StringField('Email', validators=[DataRequired(),Email()])
    picture = FileField('Employee Photo', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')

class SearchEmployeeForm(FlaskForm):

    keywords = StringField('')
    search = SubmitField('Search')
