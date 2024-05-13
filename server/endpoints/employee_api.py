from flask import request
from models.employee import Employee
from models.databaseconfig import db

def register_employee():
    from app import bcrypt
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

    return {"message": "Employee created successfully"}, 201


def delete_employee():
    data = request.get_json()
    id = data.get('id')
    employee = Employee.query.filter_by(id=id).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
        

def patch_employee():
    data = request.get_json()
    id = data.get('id')
    employee = Employee.query.filter_by(id=id).first()
    if employee:
        for key, value in data.items():
            setattr(employee, key, value)
        db.session.commit()
        
    # username = db.Column(db.String(80), unique=True, nullable=False)
    # department = db.Column(db.String(80), nullable=False)
    # address = db.Column(db.String(80), nullable=False)
    # email = db.Column(db.String(20), unique=True)
    # phonenumber = db.Column(db.String(80), nullable=False)
    # password = db.Column(db.String(80), nullable=False)
    