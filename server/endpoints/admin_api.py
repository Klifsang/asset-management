from flask import request
from models.admin import Admin
from models.databaseconfig import db

def register_admin():
    from app import bcrypt
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    usernames = data.get('usernames')
    phonenumber = data.get('phonenumber')
    address = data.get('address')
    role = data.get('role')
    
    admin = Admin(email=email, password=bcrypt.generate_password_hash(password), username=usernames, phonenumber=phonenumber, address=address, role=role)
    db.session.add(admin)
    db.session.commit()
    return {"message": "Admin added successfully"}, 201 
def delete_admin():
    data = request.get_json()
    id = data.get('id')
    admin = Admin.query.filter_by(id=id).first()
    if admin:
        db.session.delete(admin)
        db.session.commit()
    return {"message": "Admin deleted successfully"}, 201   

def patch_admin():
    data = request.get_json()
    id = data.get('id')
    admin = Admin.query.filter_by(id=id).first()
    if admin:
        for key, value in data.items():
            setattr(admin, key, value)
        db.session.commit()
    return {"message": "Admin updated successfully"}, 201   

def get_admins():
    admins = Admin.query.all()
    if admins:
        return [
            {
                "id": admin.id,
                "username": admin.username,
                "email": admin.email,
                "phonenumber": admin.phonenumber,
                "address": admin.address,
                "role": admin.role,
            }
            for admin in admins
        ]

    # username = db.Column(db.String(20), unique=True)
    # password = db.Column(db.String(255))  # Increased length
    # email = db.Column(db.String(255), unique=True)  # Increased length
    # phonenumber = db.Column(db.String(20), unique=True)
    # address = db.Column(db.String(255))  # Increased length
    # role = db.Column(db.String(50))  # Increased length