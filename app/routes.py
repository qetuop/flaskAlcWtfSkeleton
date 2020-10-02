from app import app, db
from flask import render_template
from app.models import Employee
from app.forms import EmployeeForm
from app.EmployeeData import EmployeeData

@app.route('/')
def index():
    print('index')
    employees = Employee.query.all()
    form = EmployeeForm()

    '''
    # use Python class to fill in form
    emps = []
    for emp in employees:       
        empData = EmployeeData(emp.id, emp.name, emp.age, emp.date)
        emps.append(empData)
            
    return render_template('index.html',form=form, employees=emps)
    '''
    
    # use sqlAlch class to fill in form
    return render_template('index.html',form=form, employees=employees)

