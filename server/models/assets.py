from sqlalchemy_serializer import SerializerMixin
from server.app import db

class Assets(db.Model, SerializerMixin):
    __tablename__ = 'assets'
    
    id = db.Column(db.Integer, primary_key=True)
    assetname = db.Column(db.String)
    description = db.Column(db.String)
    condition = db.Column(db.String)
    availability = db.Column(db.String, default="available")
    quantity = db.Column(db.Integer)
    
    requests = db.relationship('Requests', back_populates='asset')