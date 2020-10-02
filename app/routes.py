from app import app, db
from flask import render_template
from app.models import Employee
from app.forms import EmployeeForm

@app.route('/')
def index():
    print('index')
    employees = Employee.query.all()
    print(employees[0].id)
    form = EmployeeForm()
    return render_template('index.html',form=form, employees=employees)

