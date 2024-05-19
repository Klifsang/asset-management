from sqlalchemy_serializer import SerializerMixin
from app import db

class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admin'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(255))
    authcode = db.Column(db.String(80))
    email = db.Column(db.String(255), unique=True)
    phonenumber = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(255)) 
    role = db.Column(db.String(50))
    level = db.Column(db.String(50))
    
    employees = db.relationship('Employee', back_populates='admin')
    requests = db.relationship('Requests', back_populates='admin')