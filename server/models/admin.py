from sqlalchemy_serializer import SerializerMixin
from server.app import db

class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admin'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    authcode = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phonenumber = db.Column(db.String, unique=True)
    address = db.Column(db.String) 
    role = db.Column(db.String)
    level = db.Column(db.String)
    
    employees = db.relationship('Employee', back_populates='admin')
    requests = db.relationship('Requests', back_populates='admin')