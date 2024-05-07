from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from app import db

class Requests(db.Model,SerializerMixin):
    __tablename__ ='requests'
    
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    admin_id = db.Column(db.Integer)
    comment = db.Column(db.String)
    status = db.Column(db.String)
    assigneddate = db.Column(db.Date)
    returndate = db.Column(db.Date)
    returnstatus = db.Column(db.String)
    
# Table Requests {
#   id integer
#   asset_id integer
#   user_id integer
#   admin_id integer
#   comment string
#   status varchar
#   assigneddate date
#   returndate date
# }