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
    
    employee = Employee(username=username, department=department, address=address,email=email,phonenumber=phonenumber,password=bcrypt.generate_password_hash(password))
    
    db.session.add(employee)
    db.session.commit()

    return {"message": "Employee created successfully"}, 201

def login_employee():
    print(session.get("user_id"))
    from app import bcrypt
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    user = Employee.query.filter_by(username=username).first()

    if user is None:
        return jsonify({"error": "Unauthorized"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Username or password incorrect"}), 401
    
    session["user_id"] = user.id
    print(session.get("user_id"))
    get_current_user()
    return jsonify({
        "id": user.id,
        "username": user.username,
    }), 200
    


def get_current_user():
    user_id = session.get("user_id")
    print(user_id)
    if user_id is None:
        return jsonify({"error": "Unauthorizeduu"}), 401
    
    # user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user_id,
    }) 
    
def logout_employee():
    session.pop("user_id", None)
    return jsonify({"message": "Logged out successfully"}), 200




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
    