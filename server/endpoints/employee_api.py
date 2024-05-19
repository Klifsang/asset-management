from flask import jsonify, request, session
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
    role = data.get('role')
    status = "pending"
    employee = Employee(username=username, department=department, address=address,email=email,phonenumber=phonenumber,password=bcrypt.generate_password_hash(password), role=role, status=status)
    
    db.session.add(employee)
    db.session.commit()

    return {"message": "Employee created successfully"}, 201


def delete_employee():
    id = session.get("user_id") # session is used to avoid id injection
    employee = Employee.query.filter_by(id=id).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
    return {"message": "Employee deleted successfully"}, 201

def patch_employee():
    data = request.get_json()
    id = data.get("id")
    employee = Employee.query.filter_by(id=id).first()
    if employee:
        for key, value in data.items():
            # print(key, value)
            if key == "status" and session["user_level"] !="admin":
                return {"message": "Admin can only approve"}, 401
            if key == "status" and session["user_level"] =="admin":
                setattr(employee, "admin_id", session["user_id"])
            setattr(employee, key, value) if key != 'id' else None
        db.session.commit()
    return {"message": "Employee updated successfully"}, 201 

def get_employees():
    employees = Employee.query.all()
    if employees:
        return [
            {
                "id": employee.id,
                "username": employee.username,
                "department": employee.department,
                "address": employee.address,
                "email": employee.email,
                "phonenumber": employee.phonenumber,
                "status": employee.status
            }
            for employee in employees
        ]
        
def getstaff():
    data = request.get_json()
    id = data.get("id")
    employee = Employee.query.filter_by(id=id).first()
    print (employee)
    return jsonify({
        "id": employee.id,
        "username": employee.username,
        "department": employee.department,
        "address": employee.address,
        "email": employee.email,
        "phonenumber": employee.phonenumber,
        "status": employee.status,
        "role": employee.role,
        "admin_id": employee.admin_id
    }), 200