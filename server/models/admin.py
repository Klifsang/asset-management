
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from databaseconfig import db

class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admin'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(20), unique=True)
    phonenumber = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(100))
    role = db.Column(db.String(20))


# Table Admin {
#   id integer
#   username varchar
#   email varchar
#   position varchar
#   address varchar
#   phonenumber varchar
# }