from flask import request
from ..models.admin import Admin
from ..models.databaseconfig import db
def register_admin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    usernames = data.get('usernames')
    phonenumber = data.get('phonenumber')
    address = data.get('address')
    role = data.get('role')
    
    admin = Admin(email=email, password=password, username=usernames, phonenumber=phonenumber, address=address, role=role)
    db.session.add(admin)
    db.session.commit()
    
    # username = db.Column(db.String(20), unique=True)
    # password = db.Column(db.String(255))  # Increased length
    # email = db.Column(db.String(255), unique=True)  # Increased length
    # phonenumber = db.Column(db.String(20), unique=True)
    # address = db.Column(db.String(255))  # Increased length
    # role = db.Column(db.String(50))  # Increased length