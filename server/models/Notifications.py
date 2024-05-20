from sqlalchemy_serializer import SerializerMixin
from server.app import db

class Notifications(db.Model, SerializerMixin):
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('requests.id'), default=1)
    user_id = db.Column(db.Integer)
    asset_id = db.Column(db.Integer)
    status = db.Column(db.String)