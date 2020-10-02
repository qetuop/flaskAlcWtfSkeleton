from flask_wtf import FlaskForm
from wtforms import StringField
#from app.models import Employee

class EmployeeForm(FlaskForm):
    id = StringField('ID')
    date = StringField('Date')
    name = StringField('Name')
    age =  StringField('Age')
