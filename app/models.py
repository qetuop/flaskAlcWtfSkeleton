from app import db
from datetime import datetime

class Employee(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String(120))
    age  = db.Column(db.Integer)
