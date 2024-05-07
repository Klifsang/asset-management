from sqlalchemy_serializer import SerializerMixin
from app import db

class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admin'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(255))  # Increased length
    email = db.Column(db.String(255), unique=True)  # Increased length
    phonenumber = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(255))  # Increased length
    role = db.Column(db.String(50))  # Increased length
    
    requests = db.relationship("Requests", backref="admin")
    def __repr__(self):
        return f"<Admin {self.username}>"


# Table Admin {
#   id integer
#   username varchar
#   email varchar
#   position varchar
#   address varchar
#   phonenumber varchar
# }