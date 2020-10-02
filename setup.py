from flask_sqlalchemy import SQLAlchemy
from app.models import Employee
from app import db
from datetime import datetime

def setup():
    print('setup()')

    print('drop_all')
    db.drop_all()

    print('create_all')
    db.create_all()
    
    emp = Employee(name="Bobby", age=24, date=datetime.now())
    db.session.add(emp)
    emp = Employee(name="Sue", age=43, date=datetime.now())
    db.session.add(emp)

    print('commit')
    db.session.commit()

if __name__ == '__main__':
    setup()
