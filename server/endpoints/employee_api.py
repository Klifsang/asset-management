from flask import request
from ..models.employee import Employee
from ..models.databaseconfig import db
from app import bcrypt
def employee():
    data = request.get_json()
    username = data.get('username')
    department = data.get('department')
    address = data.get('address')
    email = data.get('email')
    phonenumber = data.get('phonenumber')
    password = data.get('password')
    
    employee = Employee(username=username, department=department, address=address,email=email,phonenumber=phonenumber,password=bcrypt.generate_password_hash(password))
    
    db.session.add(employee)
    db.session.commit()
    # username = db.Column(db.String(80), unique=True, nullable=False)
    # department = db.Column(db.String(80), nullable=False)
    # address = db.Column(db.String(80), nullable=False)
    # email = db.Column(db.String(20), unique=True)
    # phonenumber = db.Column(db.String(80), nullable=False)
    # password = db.Column(db.String(80), nullable=False)
    