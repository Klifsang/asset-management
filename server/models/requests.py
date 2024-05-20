from sqlalchemy_serializer import SerializerMixin
from server.app import db

class Requests(db.Model, SerializerMixin):
    __tablename__ ='requests'
    
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'),default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('employees.id'), default=1)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), default=1)
    comment = db.Column(db.String, default='ASAP')
    quantity = db.Column(db.Integer)
    status = db.Column(db.String, default='pending')
    assigneddate = db.Column(db.Date)
    returndate = db.Column(db.Date)
    returnstatus = db.Column(db.String)
    
    asset = db.relationship('Assets', back_populates='requests')
    employee = db.relationship('Employee', back_populates='requests')
    admin = db.relationship('Admin', back_populates='requests')