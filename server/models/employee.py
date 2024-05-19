from sqlalchemy_serializer import SerializerMixin
from app import db
    
class Employee(db.Model, SerializerMixin):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    department = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), unique=True)
    phonenumber = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    level = db.Column(db.String(50))
    status = db.Column(db.String)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # Relationship with Admin

    admin = db.relationship("Admin", back_populates="employees")  # Relationship definition
    requests = db.relationship('Requests', back_populates='employee')