from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Assets(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    assetname = db.Column(db.String)
    condition = db.Column(db.String)
    availability = db.Column(db.String)
    

# Table Assets {
#   id integer
#   assetname varchar
#   condition varchar
#   availability varchar
# }