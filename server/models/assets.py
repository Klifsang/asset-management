from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from app import db

class Assets(db.Model, SerializerMixin):
    __tablename__ = 'assets'
    
    id = db.Column(db.Integer, primary_key=True)
    assetname = db.Column(db.String)
    description = db.Column(db.String)
    condition = db.Column(db.String)
    availability = db.Column(db.String)
    
    # requests = db.relationship("Requests", backref="assets")
    
# Table Assets {
#   id integer
#   assetname varchar
#   condition varchar
#   availability varchar
# }